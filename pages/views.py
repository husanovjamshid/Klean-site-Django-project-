from django.contrib import messages
from django.shortcuts import render
from .models import Post, Comment, Category, Contact, CategoryImg, PostImg
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

def project(request):
    catImg = CategoryImg.objects.all()
    posts = PostImg.objects.all()

    return render(request, 'project.html',
                  context={
                      'catImg':catImg,
                      'posts':posts
                  })



def contact(request):
    contact = Contact()

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.message = message
            contact.save()


            messages.success(request, 'Xabaringiz muvaffaqqiyatli yetkazildi!!!')
        except:
            messages.error(request, 'Xabaringiz yuborilmadi!!!')


    return render(request, 'contact.html',
                  context={

                  }
                  )

def category(req, id):
    posts = Post.objects.filter(cat_id=id)

    return render(req, 'category.html',
                  context={
                      'posts': posts,


                  })