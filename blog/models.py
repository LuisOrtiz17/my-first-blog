from django.db import models
from django.utils import timezone

class Post(models.Model):
    #este es una relación (link) con otro modelo.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #así es como defines un texto con un número limitado de caracteres.
    title = models.CharField(max_length=200)
    #este es para texto largo sin límite. Suena perfecto para el contenido de la
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #este es fecha y hora.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
