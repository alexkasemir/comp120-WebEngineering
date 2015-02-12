from django.http import HttpResponse
from django.template import RequestContext, loader
from meows.models import User_Post

def index(request):
    latest_posts = User_Post.objects.order_by('time_created')[:5]
    template = loader.get_template('meows/index.html')
    context = RequestContext(request, {
        'latest_posts': latest_posts,
    })
    return HttpResponse(template.render(context))
