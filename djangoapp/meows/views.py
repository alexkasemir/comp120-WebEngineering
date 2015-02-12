from django.http import HttpResponse

from meows.models import User_Post

def index(request):
    latest_posts = User_Post.objects.order_by('time_created')[:5]
    output = ', '.join([p.text_content for p in latest_posts])
    return HttpResponse(output)

