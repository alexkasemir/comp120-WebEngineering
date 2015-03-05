from django.http import HttpResponse
from django.template import RequestContext, loader
from meows.models import User_Post
from django.http import HttpResponseRedirect
from purrer.settings import MEDIA_ROOT

from django.http import Http404
from django.shortcuts import render

from django.core.urlresolvers import reverse

def index(request):
    latest_posts = User_Post.objects.order_by('-time_created')[:10]
    template = loader.get_template('meows/Pages/index.html')
    context = RequestContext(request, {
        'latest_posts': latest_posts,
    })
    return HttpResponse(template.render(context))

def detail(request, user_post_id):
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    return render(request, 'meows/Pages/detailsPage.html', {'user_post': user_post, 'count': user_post_id})

def new_post(request):
    return render(request, 'meows/Pages/new_post.html')

def handle_uploaded_file(f):
    dest = open(MEDIA_ROOT + '/images/' + f.name, 'wb+')
    for chunk in f.chunks():
        dest.write(chunk)

def create_post(request):
    print(request.FILES)
    image = request.FILES['image_URL']
    user_post = User_Post.create(request.POST.get('text_content'))
    handle_uploaded_file(image)
    user_post.image_URL = image.name
    print(user_post)
    user_post.save()
    return render(request, 'meows/Pages/details.html', {'user_post': user_post})

def post_like(request, user_post_id):
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
        print("Score is: ")
        print(user_post.score)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    user_post.score += 1
    user_post.save()
    return HttpResponse(status=201)

def post_dislike(request, user_post_id):
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
        print("Score is: ")
        print(user_post.score)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    user_post.score -= 1
    user_post.save()
    return HttpResponse(status=201)
