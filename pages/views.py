from django.shortcuts import render
from .models import Post, Comment, Category
# Create your views here.

def index(req):
    posts = Post.objects.all()
    # Category
    cat = Category.objects.all()
    return render(req, 'index.html',
                  context={
                      'posts':posts,
                      'cat':cat
                  })

def about(req):
    posts = Post.objects.all()
    return render(req, 'about.html')

def service(req):
    posts = Post.objects.all()
    return render(req, 'service.html')

def project(req):
    posts = Post.objects.all()
    return render(req, 'project.html')

def contact(req):
    posts = Post.objects.all()
    return render(req, 'contact.html')

def blog(req):
    posts = Post.objects.all()
    return render(req, 'blog.html',
                  context={
                      'posts':posts
                  })


def blog_detail(req, id):

    # Comment
    comment = Comment.objects.all()


    # filter by id
    posts = Post.objects.get(id=id)

    # Order by
    post_2 = Post.objects.all().order_by('-view_count')

    # View count
    posts.view_count+=1
    posts.save()

    # Category
    cat = Category.objects.all()


    return render(req, 'blog_detail.html',
                  context={
                      'posts': posts,
                      'comment': comment,
                      'post_2': post_2,
                      'cat': cat,


                  })