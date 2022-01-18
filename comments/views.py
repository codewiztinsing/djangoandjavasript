from django.shortcuts import render
from posts.models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404,redirect

def post_detail(request, pk):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, pk = pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user.first_name + " " + request.user.last_name
            # Save the comment to the database
            new_comment.save()
            return redirect("post:list")
    else:
        comment_form = CommentForm()

    return render(request, "comments/detail.html", {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})