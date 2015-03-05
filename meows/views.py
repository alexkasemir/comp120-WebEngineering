from django.http import HttpResponse
from django.template import RequestContext, loader
from meows.models import User_Post
from django.http import HttpResponseRedirect
from purrer.settings import MEDIA_ROOT
from django.core.cache import cache

from django.http import Http404
from django.shortcuts import render

from django.core.urlresolvers import reverse


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
    return render(request, 'meows/Pages/details.html', {'user_post': user_post})

def new_post(request):
    return render(request, 'meows/Pages/new_post.html')

def handle_uploaded_file(f):
    dest = open(MEDIA_ROOT + '/images/' + f.name, 'wb+')
    for chunk in f.chunks():
        dest.write(chunk)
    dest.close()

def create_post(request):
    print(request.FILES)
    user_post = User_Post.create(request.POST.get('text_content'))
    if(request.FILES):
        image = request.FILES['image_URL']
        handle_uploaded_file(image)
        user_post.image_URL = image.name
    else:
        user_post.image_URL = ''
    print(user_post)
    user_post.save()
    cache.delete("latest_posts")
    return render(request, 'meows/Pages/details.html', {'user_post': user_post})


