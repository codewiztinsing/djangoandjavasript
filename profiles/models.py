from django.db import models
from CustomUser.models import User
from django.utils.translation import gettext as _
from django.conf.urls.static import static
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver



def handle_upload_profile_pic(instance, filename):
    return f"profiles/avatars_{instance.lead.pk}/{filename}"




class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]



    COORDINATOR = 1
    TRAINEE = 2
    ROLE_CHOICES = [
        (COORDINATOR, _("Coordinator")),
        (TRAINEE, _("Trainee")),
    ]


    user     = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar   = models.ImageField(upload_to=handle_upload_profile_pic, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender   = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone    = models.CharField(max_length=32, null=True, blank=True)
    address  = models.CharField(max_length=255, null=True, blank=True)
    role     = models.PositiveSmallIntegerField(choices = ROLE_CHOICES, null=True, blank=True)
    city     = models.CharField(max_length=50, null=True, blank=True)
    zip      = models.CharField(max_length=30, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')

    def __str__(self):
        return f"profile of {self.user.username}"
@receiver(post_save,sender = User)
def pre_save_profile_create(sender,instance,created,*args,**kwargs):
    if created:
        print("created",created)
        Profile.objects.create(user = instance)
