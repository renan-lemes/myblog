from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    # Unico id ou seja cada post vai ter um unico slug#
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #vai armazenar cada tipo de author #
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    #adiciona a data e a hora #
    updated = models.DateTimeField(auto_now=True)
    #vai atualizar cada campo #

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug}) 