from django.http import HttpResponse
from django.template import RequestContext, loader
from meows.models import User_Post, UserPostForm
from django.http import HttpResponseRedirect
from purrer.settings import MEDIA_URL
from django.http import Http404
from django.shortcuts import render

from django.core.urlresolvers import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from meows.serializers import PostSerializer

def index(request):
    posts = cache.get("latest_posts")
    if not posts:
        posts = User_Post.objects.order_by('-time_created')[:10]
        cache.set("latest_posts", posts)
    # latest_posts = User_Post.objects.order_by('-time_created')[:10]
    template = loader.get_template('meows/Pages/index.html')
    context = RequestContext(request, {
        'latest_posts': posts,
    })
    return HttpResponse(template.render(context))

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

def create_post(request):
    # filename = '%s%s' % (MEDIA_URL, request.FILES['image_URL'].name)
    # print(filename)
    # post = User_Post(image_URL=filename)
    form = UserPostForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
        user_post = form.save()
        return render(request, 'meows/Pages/details.html', {'user_post': user_post})
    else:
        user_post.image_URL = ''
    print(user_post)
    user_post.save()
    cache.delete("latest_posts")
    return render(request, 'meows/Pages/detailsPage.html', {'user_post': user_post})


def post_like(request, user_post_id):
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    user_post.score += 1
    user_post.save()
    cache.delete("latest_posts")
    return HttpResponse(status=201)

def post_dislike(request, user_post_id):
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
        posts = User_Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'image_URL': request.FILES['image_URL'], 'text_content': request.POST.get('text_content'), 'score': 0, }

        data = {'text': request.DATA.get('the_post'), 'author': request.user.pk}
        fields = ('image_URL', 'text_content', 'score', 'time_created', 'time_edited')

@api_view(['GET'])
def api_post_element(request, user_post_id):
    try:
        post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

