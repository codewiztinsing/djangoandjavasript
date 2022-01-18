from CustomUser.views import SignupView
from profiles.views import ProfileView
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .views import DashboardView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', DashboardView.as_view(),name = "dash-board"),
    path('signup/', SignupView.as_view(),name = 'signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('comments/', include("comments.urls",namespace = "comments")),
    path('', include("posts.urls",namespace = "post")),
   

]
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)