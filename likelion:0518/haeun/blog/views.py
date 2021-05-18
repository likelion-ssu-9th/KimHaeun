from django.shortcuts import ,get_object_or_404
from .models import blog
# Create your views here.
def home(request):
    blogs=blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request, id):
    blog=get_object_or_404(blog,pk=id)
    return render(request,'detail.html',{'blog':blog})