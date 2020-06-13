from django.shortcuts import render , redirect , get_object_or_404
from django.utils import timezone
from .models import Blog
from .form import NewBlog



# Create your views here.
def welcome(request):
    return render(request, 'blog/home.html')

def read(request):
    blogs=Blog.objects.all()
    return render(request,'blog/home.html',{'blogs':blogs})

def create(request):
    if request.method == 'POST':
        blogs=Blog()
        blogs.photo=request.FILES['photo']
        blogs.title=request.POST['title']
        blogs.body=request.POST['body']
        blogs.pub_date= timezone.now()
        blogs.save()
            
        return redirect('home')

    else:
        
        return render(request , 'blog/new.html ')
    return

def update(request,pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = NewBlog(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.title=request.POST['title']
            blog.photo=request.FILES['photo']
            blog.body=request.POST['body']
            blog.pub_date= timezone.now()
            blog.save()
            return redirect('blog/detail',pk=blog.pk)
    else:
        form=NewBlog(instance=blog)
        return render(request,'blog/update.html',{'form':form})
'''
def update(request,pk):
    blog = get_object_or_404(Blog, pk=pk)

    form = NewBlog(request.POST , instance=blog)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'viewcrud/new.html',{'form':form})'''


def delete(request,pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})


