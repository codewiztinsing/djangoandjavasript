from django.db import models
# from django.contrib.auth.models import User
from CustomUser.models import User
from profiles.models import Profile
from django.core.validators import FileExtensionValidator


def get_file_path(filename,instance):
    ext = filename.split('.')[-1]
    filename = "/static/images/%s.%s" % (instance, ext)

    return filename

class Post(models.Model):
    title   = models.CharField(max_length = 200)
    body    = models.TextField()
    liked   = models.ManyToManyField(User,blank = True)
    author  = models.ForeignKey(Profile,on_delete = models.CASCADE)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    images = models.ImageField(upload_to = 'images',blank = True,null = True)
    video   = models.FileField(upload_to='videos',null=True,
                                     validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])


    @property
    def like_count(self):
        return self.liked.all().count()


    @property
    def get_image(self):
        return self.images.url

    @property
    def get_video(self):
        return self.video.url
    
    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-created"]