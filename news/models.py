from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='news_images/',
        null=True,
        blank=True
    )
    is_breaking = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title