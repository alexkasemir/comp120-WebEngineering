from django.http import HttpResponse
from django.template import RequestContext, loader

from meows.models import User, User_Post, Feedback, Hashtag, Preference

import time

from django.http import HttpResponseRedirect
#from purrer.settings import MEDIA_ROOT
from django.core.cache import cache

from django.http import Http404
from django.shortcuts import render, render_to_response, redirect

from django.core.urlresolvers import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from meows.serializers import PostSerializer
from meows.serializers import UserSerializer

from django.core.cache import cache

from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required

from meows.forms import AuthenticationForm, RegistrationForm
import json
from meows.purrtags import tags
from meows.purrtags import my_posts
from meows.forms import UserPostForm
from meows.purrtags import tagManager



@login_required
def index(request):
    manager = tagManager()
    user = request.user
    #my_hashtags = Preference.objects.filter(user_id=user)
    liked = User_Post.objects.filter(purrs_grrs=user)
    #disliked = User_Post.objects.filter(grrs=user)
    #most_recent = User_Post.objects.order_by('-id')[0]
    posts = cache.get("latest_posts")

    form = UserPostForm()
    #print posts

    feedback = cache.get("feedback")
    if (not posts):  # new post has been created
        posts = User_Post.objects.order_by('-id')[:20]
        cache.set("latest_posts", posts)

        # template = loader.get_template('meows/Pages/index.html')
        # context = RequestContext(request, {
        #     'latest_posts': posts,
    # if most_recent.pk > posts[0].pk:
    #     posts = User_Post.objects.order_by('-id')[:20]
    #     cache.set("latest_posts", posts)
    if not feedback:
        feedback = Feedback.objects.filter(post_id=posts)

    recent_hashtags = Hashtag.objects.filter(user_post=posts).order_by('-count')
    trending = []
    last_hashtag = 0
    for hashtag in recent_hashtags:
        if hashtag.pk is not last_hashtag:
            trending.append(hashtag.content)
            last_hashtag = hashtag.pk
    cache.delete("trending")
    cache.set("trending", trending)

    my_hashtags = Preference.objects.filter(user_id=user).order_by('-score')[:5]
    my_tags = []
    for hashtag in my_hashtags:
        #h = Hashtag.objects.get(pk=hashtag.hashtag_id)
        my_tags.append(hashtag.hashtag_id.content)
    cache.delete("my_tags")
    cache.set("my_tags", my_tags)
    # trending = []
    # for post in posts:
    #     trending.extend(post.hashtags.all())
    #     print trending
    # t = trending.order_by('score')[:5]
    #pop_hashtags = posts.hashtags.order_by(score)[:5]
    #print pop_hashtags
    #my_preferences = manager.select_posts(my_hashtags, posts)
    #print my_preferences
    return render(request, 'meows/Pages/index.html', {'latest_posts': posts, 'liked_posts': liked, 'feedback': feedback, 'form': form, 'trending_tags': trending, 'my_tags':my_tags})

@login_required
def user_pref(request):
    trending = cache.get("trending")
    my_tags = cache.get("my_tags")
    manager = tagManager()
    form = UserPostForm()
    user = request.user
    posts = User_Post.objects.order_by('-id')[:100]
    my_hashtags = Preference.objects.filter(user_id=user)
    my_preferences = manager.select_posts(my_hashtags, posts)
    return render(request, 'meows/Pages/hashtag_index.html', {'latest_posts': my_preferences, 'form': form, 'user': user, 'trending_tags': trending, 'my_tags':my_tags})


@login_required
def user_index(request, user):
    trending = cache.get("trending")
    my_tags = cache.get("my_tags")
    form = UserPostForm()
    try: 
        posts = User_Post.objects.filter(creator=user)
    except User_Post.DoesNotExist:
        return render(request, 'meows/Pages/hashtag_index.html', {'form': form, 'user': user})

    return render(request, 'meows/Pages/hashtag_index.html', {'latest_posts': posts, 'form': form, 'user': user, 'trending_tags': trending, 'my_tags':my_tags})

@login_required
def hashtag_index(request, tag):
    form = UserPostForm()
    trending = cache.get("trending")
    my_tags = cache.get("my_tags")
    try:
        hashtag = Hashtag.objects.get(content=tag)
    except Hashtag.DoesNotExist:
        return render(request, 'meows/Pages/hashtag_index.html', {'form': form, 'tag': tag})
    
    posts = User_Post.objects.filter(hashtags=hashtag)
    return render(request, 'meows/Pages/hashtag_index.html', {'latest_posts': posts, 'form': form, 'tag': tag, 'trending_tags': trending, 'my_tags':my_tags})

@login_required
def detail(request, user_post_id):
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    return render(request, 'meows/Pages/detailsPage.html', {'user_post': user_post, 'count': user_post_id})


@login_required
def new_post(request):
    form = UserPostForm()
    return render(request, 'meows/Pages/new_post.html', {'form': form})

# def handle_uploaded_file(f):
#     dest = open(MEDIA_ROOT + '/images/' + f.name, 'wb+')
#     for chunk in f.chunks():
#         dest.write(chunk)
#     dest.close()


@login_required
def create_post(request):
    # print(request.FILES)
    # user_post = User_Post.create(request.POST.get('text_content'))
    # if(request.FILES):
    #     image = request.FILES['image_URL']
    #     handle_uploaded_file(image)
    #     user_post.image_URL = image.name
    # else:
    #     user_post.image_URL = ''
    # print(user_post)
    # user_post.save()
    # cache.delete("latest_posts")
    # return render(request, 'meows/Pages/detailsPage.html', {'user_post': user_post})
    #post = User_Post()
    manager = tagManager()
    user = request.user
    form = UserPostForm(request.POST, request.FILES)

    if form.is_valid():
        user_post = form.save(commit=False)
        user_post.creator = user
        user_post.save()
        cache.delete("latest_posts")
        form.save_m2m()
        manager.postCreated(user, user_post)
        return redirect('/')
        #return render(request, 'meows/Pages/detailsPage.html', {'user_post': user_post})
    else:
        return render(request, 'meows/Pages/new_post.html', {'form': form})


@login_required
def post_like(request, user_post_id):
   # print "LIKE!!!!!\n\n\n\n\n\n"
    manager = tagManager()
    user = request.user
    # print user
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")

    did_purr = user_post.purrs_grrs.filter(pk=user_post_id)
    if did_purr:
        print "You can't purr that"
        return HttpResponse(status=401)
    else:
        feedback = Feedback(post_id=user_post, user_id=user, purr_grr='p')
        feedback.save()
        cache.delete("latest_posts")
        #user_post.purrs.add(user)
        user_post.score += 1
        user_post.save()
        cache.delete("feedback")
        manager.postLiked(user, user_post)
        return HttpResponse(status=201)


@login_required
def post_dislike(request, user_post_id):
   # print "DISLIKE!!!!!\n\n\n\n\n\n"
    manager = tagManager()
    user = request.user
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")

    did_grr = user_post.purrs_grrs.filter(pk=user.pk)
    if did_grr:
        print "no"
        return HttpResponse(status=401)
    else:
        cache.delete("latest_posts")
        feedback = Feedback(post_id=user_post, user_id=user, purr_grr='g')
        feedback.save()
        # print user_post.purrs_grrs.all()
        user_post.score -= 1
        user_post.save()
        cache.delete("feedback")
        manager.postDisliked(user, user_post)
        return HttpResponse(status=201)




#create new user form
#create new user
def register_user(request):
    form = RegistrationForm()

    for field in form.fields:
        field.widget.attrs = {'class':'form_control'}
    return render(request, 'meows/Pages/register.html', {'form': form})


def register(request):
    #return render(request, 'meows/Pages/register.html')
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
        for field_name, field in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
    return render_to_response('meows/Pages/register.html', {'form': form}, context_instance=RequestContext(request))


def login_user(request):
    form = AuthenticationForm()
    for field_name, field in form.fields.items():
        field.widget.attrs['class'] = 'form-control'
    return render(request, 'meows/Pages/login.html', {'form': form})


def login(request):
    #return render(request, 'meows/Pages/login.html')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
    else:
        form = AuthenticationForm()
        for field_name, field in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
    return render_to_response('meows/Pages/login.html', {'form': form}, context_instance=RequestContext(request))


def logout(request):
    django_logout(request)
    return redirect('/')


#API Functionality
@login_required
@api_view(['GET', 'POST'])
def api_post_collection(request):
    if request.method == 'GET':
        posts = User_Post.objects.order_by('-time_created')[:20]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user_post = {"text_content": request.DATA.get('text_content'), "score": '0', }
        serializer = PostSerializer(data=user_post)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_post_group(request, user_post_id):
    posts = User_Post.objects.filter(pk__lt=user_post_id)[:20]
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def api_post_element(request, user_post_id):
    try:
        post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def api_user_collection(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        user_info = {"username": request.DATA.get('username'), "email": request.DATA.get('email')}
        serializer = UserSerializer(data=user_info)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_user_element(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)



def api_docs(request):
    return render(request, 'meows/Pages/apidocs.html')
