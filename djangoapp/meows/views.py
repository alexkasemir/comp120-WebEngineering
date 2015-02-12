from django.http import HttpResponse
from django.template import RequestContext, loader
from meows.models import User_Post

from django.http import Http404
from django.shortcuts import render

def index(request):
    latest_posts = User_Post.objects.order_by('time_created')[:5]
    template = loader.get_template('meows/index.html')
    context = RequestContext(request, {
        'latest_posts': latest_posts,
    })
    return HttpResponse(template.render(context))


def detail(request, user_post_id):
    try:
        user_post = User_Post.objects.get(pk=user_post_id)
    except User_Post.DoesNotExist:
        raise Http404("Post does not exist!")
    return render(request, 'meows/details.html', {'user_post': user_post})
