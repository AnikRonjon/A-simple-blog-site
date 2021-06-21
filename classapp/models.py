from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published')
)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='blogger')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category')
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    body = models.TextField()
    image = models.ImageField(upload_to='image/%y/%m', unique_for_date=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('classapp:post_detail',
                       args=[self.published.year,
                             self.published.month,
                             self.published.day,
                             self.slug]
                       )
