from django.urls import path
from .views import (load_post_data,
                     post_list_and_create
                     ,like_unlike_post,
                     post_detail_page,
                     update_post_view_data,
                     delete_post_view_data,
                     post_detail_view_data)

app_name = "posts"
urlpatterns = [
    path('',post_list_and_create, name= "list"),
    path('likeunlike/',like_unlike_post, name= "like_unlike_post"),
    path('<pk>/',post_detail_page, name= "post-detail"),
    path('<pk>/data/',post_detail_view_data, name= "post-data-detail"),
    path('<pk>/update/',update_post_view_data, name= "post-data-update"),
    path('<pk>/delete/',delete_post_view_data, name= "post-data-delete"),
    path('list/<int:num_posts>/',load_post_data, name= "post-list"),


]