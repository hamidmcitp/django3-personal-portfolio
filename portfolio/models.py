from django.db import models

class ProjectHamidBagheri(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)



# for displate title name on admin panel
    def __str__(self):
        return self.title
