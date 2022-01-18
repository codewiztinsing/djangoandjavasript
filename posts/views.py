from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from .forms import PostForm
from profiles.models import Profile
from django.contrib.auth.decorators import login_required



def post_list_and_create(request):
    
    form = PostForm(request.POST or None)
    if request.is_ajax():
        if form.is_valid():
            author = Profile.objects.get(user = request.user)
            instance = form.save(commit = False)
            instance.author = author
            instance.save()
            return JsonResponse({
                'title':instance.title,
                'body':instance.body,
                # 'author':instance.user.username,
                'id':instance.id,
                # 'image':instance.get_image,
                # 'video':instance.get_video
            })
    context = {
        'form':form
    }
   
    return render(request,"posts/main.html",context)


def post_detail_page(request,pk):
    obj = Post.objects.get(pk = pk)
    form = PostForm()

    context = {
        'obj':obj,
        'form':form
    }
    return render(request,'posts/detail.html',context)


def post_detail_view_data(request,pk):
    obj = Post.objects.get(pk = pk)
    data = {
        'id':obj.id,
        'title':obj.title,
        'body':obj.body,
        'author':obj.author.user.username,
        'logged_in':request.user.username
    }
    return JsonResponse({
        'data':data
    })


def load_post_data(request,num_posts):
    
    visible = 3
    upper = num_posts
    lower = upper -visible
    size  = Post.objects.all().count()
    data = []
    posts = Post.objects.all()
    for post in posts:
        item = {
            'id':post.id,
            'title':post.title,
            'body':post.body,
            'liked':True if request.user in post.liked.all() else False,
            'count':post.like_count,
            'author':post.author.user.username,
            'updated':post.updated,
            'created':post.created
        }
        data.append(item)

    return JsonResponse({
        'data':data[lower:upper],'size':size
    })


def like_unlike_post(request):
    if request.is_ajax():
        
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk = pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        
        return JsonResponse({
            "liked":liked,
            "count":obj.like_count
        })
   


def update_post_view_data(request,pk = None):
    if request.is_ajax():
        obj = Post.objects.get(pk = pk)
        new_title = request.POST.get("title")
        new_body = request.POST.get("body")
        obj.title = new_title
        obj.body  = new_body
        obj.save()

        return JsonResponse({
           'title':new_title,
           'body':new_body
        })
   

def delete_post_view_data(request,pk = None):
    if request.is_ajax():
        obj = Post.objects.get(pk = pk)
        obj.delete()

        return JsonResponse({
                    })