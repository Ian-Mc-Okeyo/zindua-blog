from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView



# @login_required
# def home(requests):
#     posts = Post.objects.all()
#     context = {
#         "posts": posts
#     }
#     return render(requests, "blog/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post

# def postDetail(request, pk):
#     print(pk)
#     post = Post.objects.filter(pk=pk).first()

#     return render(request, "blog/post_detail.html", {"post": post})

def createPost(request):
    pass

def about(requests):
    return render(requests, "blog/about.html")

def contactUs(requests):
    return render(requests, "blog/contact.html")