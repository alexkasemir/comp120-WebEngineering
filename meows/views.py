from django.http import HttpResponse
from django.template import RequestContext, loader
from meows.models import User, User_Post, UserPostForm
import time

from django.http import HttpResponseRedirect
#from purrer.settings import MEDIA_ROOT
from django.core.cache import cache

from django.http import Http404
from django.shortcuts import render

from django.core.urlresolvers import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from meows.serializers import PostSerializer
from meows.serializers import UserSerializer

from django.core.cache import cache

def index(request):
    posts = cache.get("latest_posts")
    if not posts: #new post has been created
        posts = User_Post.objects.order_by('-time_created')[:20]
        cache.set("latest_posts", posts)
        # template = loader.get_template('meows/Pages/index.html')
        # context = RequestContext(request, {
        #     'latest_posts': posts,
        # })
    return render(request, 'meows/Pages/index.html', {'latest_posts': posts} )

def detail(request, user_post_id):
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    return render(request, 'meows/Pages/detailsPage.html', {'user_post': user_post, 'count': user_post_id})

def new_post(request):
    form = UserPostForm()
    return render(request, 'meows/Pages/new_post.html', {'form': form})

# def handle_uploaded_file(f):
#     dest = open(MEDIA_ROOT + '/images/' + f.name, 'wb+')
#     for chunk in f.chunks():
#         dest.write(chunk)
#     dest.close()

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
    form = UserPostForm(request.POST, request.FILES)
    print(form)
    if form.is_valid(): 
        user_post = form.save(commit=False)
        print(user_post.time_edited)
        user_post.save()
        print(user_post.time_edited)
        cache.delete("latest_posts")
        form.save_m2m()
        return render(request, 'meows/Pages/detailsPage.html', {'user_post': user_post})
    else:
        return render(request, 'meows/Pages/new_post.html', {'form': form})


def post_like(request, user_post_id):
   # print "LIKE!!!!!\n\n\n\n\n\n"
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    cache.delete("latest_posts")
    user_post.score += 1
    user_post.save()

    return HttpResponse(status=201)

def post_dislike(request, user_post_id):
   # print "DISLIKE!!!!!\n\n\n\n\n\n"
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    user_post.score -= 1
    user_post.save()
    cache.delete("latest_posts")
    return HttpResponse(status=201)

#API Functionality
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
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user_info = {"username": request.DATA.get('username'), "owner_email": request.DATA.get('owner_email')}
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

