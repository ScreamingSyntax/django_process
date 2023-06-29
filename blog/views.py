from django.shortcuts import render
from django.http import HttpResponse
from  .models import Post


def home(request):

    posts = Post.objects.all()
    context = {
        'post':posts,
        'title':'home'
    }
    # return HttpResponse('<h1>BlogHome</h1>')4
    return render(request, 'blog/home.html',context)
# Create your views here.
def about(request):
    return render(request,'blog/about.html')