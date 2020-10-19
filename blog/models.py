from django.db import models

class BlogHamidBagheri(models.Model):
    title = models.CharField(max_length=200)
    date= models.DateField()
    description = models.TextField()

# for displate title name on admin panel
    def __str__(self):
        return self.title
