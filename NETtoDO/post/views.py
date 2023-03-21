from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddPostForm
from .models import Post, Days


def home_page(request):
    posts = Post.objects.all()
    days = Days.objects.all()
    return render(request,'post/index.html',{'posts' : posts, 'days' : days})


def show_day(request, day_id):
    posts = Post.objects.filter(day=day_id)
    days = Days.objects.all()
    return render(request, 'post/show.html', {'posts':posts, 'days' : days})


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddPostForm()
    return render(request,'post/add_post.html',{'form':form})
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home_page')


class PostForm:
    pass


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(request.POST or None, instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})