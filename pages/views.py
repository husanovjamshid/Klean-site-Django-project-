from django.shortcuts import render
from .models import Post, Comment
# Create your views here.

def index(req):
    posts = Post.objects.all()
    return render(req, 'index.html',
                  context={
                      'posts':posts
                  })

def about(req):
    posts = Post.objects.all()
    return render(req, 'about.html',
                  context={
                      'posts':posts
                  })

def service(req):
    posts = Post.objects.all()
    return render(req, 'service.html',
                  context={
                      'posts':posts
                  })

def project(req):
    posts = Post.objects.all()
    return render(req, 'project.html',
                  context={
                      'posts':posts
                  })

def contact(req):
    posts = Post.objects.all()
    return render(req, 'contact.html',
                  context={
                      'posts':posts
                  })

def blog(req):
    posts = Post.objects.all()
    return render(req, 'blog.html',
                  context={
                      'posts':posts
                  })

def blog_detail(req, id):
    comment = Comment.objects.all()
    news = Post.objects.all()
    posts = Post.objects.get(id=id)
    return render(req, 'blog_detail.html',
                  context={
                      'posts':posts,
                      'news': news,
                      'comment':comment
                  })