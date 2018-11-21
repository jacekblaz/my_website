from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Tab(models.Model):
    name = models.CharField(max_length=50, default='tab')

    def __str__(self):
        return self.name


class Article(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, default='title')
    lead = models.CharField(max_length=200, default='lead')
    article_text = RichTextUploadingField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True)


    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='articles', default='photo')


    def __str__(self):
        return self.name

class Emotion(models.Model):
    emotion = models.CharField(max_length=50)

    def __str__(self):
        return self.emotion

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class AudioSample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.title

