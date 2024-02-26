from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.pub_date = timezone.now()
            new_comment.save()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@permission_required('blog.add_post')  # Ensure the user has the required permission
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.pub_date = timezone.now()
            new_post.save()
            return redirect('post_detail', post_id=new_post.id)
    else:
        form = PostForm()

    return render(request, 'blog/new_post.html', {'form': form})

def blog_view(request):
    all_posts = Post.objects.all()

    return render(request, 'blog/blog_list.html', {'all_posts': all_posts})
