from django.db import models
from profiles.models import Profile
# Create your models here.


class CoordinatorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Coordinator(models.Model):
    profile         =     models.ForeignKey(Profile, related_name="profiles",on_delete=models.CASCADE)
    first_name      =     models.CharField(max_length=20)
    last_name       =     models.CharField(max_length=20)
    age             =     models.IntegerField(default=0)
    category        =     models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)
    description     =     models.TextField()
    phone_number    =     models.CharField(max_length=20)
    email           =     models.EmailField()
    converted_date  =     models.DateTimeField(null=True, blank=True)

    objects = CoordinatorManager()

    def __str__(self):
        return f"{self.profile.user.username}"





def handle_upload_follow_ups(instance, filename):
    return f"coordinate_followups/coordinate_{instance.coordinator.pk}/{filename}"


class FollowUp(models.Model):
    coordinator     = models.ForeignKey(Coordinator, related_name="followups", on_delete=models.CASCADE)
    date_added      = models.DateTimeField(auto_now_add=True)
    notes           = models.TextField(blank=True, null=True)
    file            = models.FileField(null=True, blank=True, upload_to=handle_upload_follow_ups)

    def __str__(self):
        return f"{self.coordinator.first_name} {self.coordinator.last_name}"




class Category(models.Model):
    name            = models.CharField(max_length=30)  # New, Contacted, Converted, Unconverted
    profile_user    = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


