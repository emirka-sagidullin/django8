from django.shortcuts import render
from .forms import section
from .models import Post

# Create your views here.

def posts(request):
    Section = section()
    return render(request, 'posts.html', {'form': Section})

def allPosts(request):
    if request.POST:
        post = Post()
        post.heading = request.POST.get('Heading')
        post.url = request.POST.get('URL')
        post.content = request.POST.get('Content')
        post.publication = request.POST.get('Publication')
        post.category = request.POST.get('Category')
        post.save()
    all = Post.objects.all()
    return render(request, 'allPosts.html', {'posts': all})