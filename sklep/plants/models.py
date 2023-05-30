from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Plants(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='plantss', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='plants_images', blank=True, null=True)

    def __str__(self):
        return self.name