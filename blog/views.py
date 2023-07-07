from django.shortcuts import render
from django.http import HttpResponse
from  .models import Post
from django.views.generic import(ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView
                                 )
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'title':'home'
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    context_object_name='posts'
    template_name='blog/home.html'
    ordering=['-posted_on']

class DetailedListView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
 
def about(request):
    return render(request,'blog/about.html')