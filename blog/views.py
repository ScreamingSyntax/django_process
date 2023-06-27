from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'Aaryan Jha',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'August 27, 2023'
    },
    {
        'author':'Ishan Kafle',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'September 27, 2023'
    }
]

def home(request):
    context = {
        'post':posts,
        'title':'home'
    }
    # return HttpResponse('<h1>BlogHome</h1>')4
    return render(request, 'blog/home.html',context)
# Create your views here.
def about(request):
    return render(request,'blog/about.html')