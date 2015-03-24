from django.http import HttpResponse
from django.template import RequestContext, loader
from meows.models import User_Post, UserPostForm
from django.http import HttpResponseRedirect
from purrer.settings import MEDIA_URL
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
        return render(request, 'meows/Pages/new_post.html', {'form': form})
