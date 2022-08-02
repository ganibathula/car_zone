from django.db import models

# Create your models here.
class Team(models.Model):
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    designation=models.CharField(max_length=300)
    photo=models.ImageField(upload_to='image/%Y/%m/%d')
    facebook_link=models.URLField(max_length=300)
    twitter_link=models.URLField(max_length=300)
    google_plus_link=models.URLField(max_length=300)
    create_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name