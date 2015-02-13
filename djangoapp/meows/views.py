from django.http import HttpResponse
from django.template import RequestContext, loader
from meows.models import User_Post
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

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
    #return render_to_response('meows/index.html', {}, context)


def detail(request, user_post_id):
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    return render(request, 'meows/Pages/details.html', {'user_post': user_post})

def new_post(request):
    return render(request, 'meows/Pages/new_post.html')

def create_post(request):
    user_post = User_Post.create(request.POST.get('text_content'))
    user_post.image_URL = request.POST.get('img_content')
    user_post.save()
    return render(request, 'meows/Pages/details.html', {'user_post': user_post})