from django.urls import path
from .views import post_detail


app_name = "comments"
urlpatterns =  [
    path('<pk>/', post_detail, name='list_comment')
]