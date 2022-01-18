from django.shortcuts import render,reverse
from .forms import CustomUserCreationForm
from django.views import generic

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("post:list")
