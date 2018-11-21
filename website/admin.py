from django.contrib import admin
from .models import Article, Tab, AudioSample, Emotion, ArticleImage
from django.forms import Textarea, TextInput
from django.db import models


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '420'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 50})},
    }


admin.site.register(Article)
admin.site.register(Tab)
admin.site.register(AudioSample)
admin.site.register(Emotion)
admin.site.register(ArticleImage)