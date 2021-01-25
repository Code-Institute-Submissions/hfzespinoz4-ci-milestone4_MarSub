from django.db import models


# Creating the categories model
class Category(models.Model):

    # Display "categories" on admin panel"
    class Meta:
        verbose_name_plural = 'Categories'

    category = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024)
    image = models.ImageField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.category


# Creating the services Model
class services(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    service = models.CharField(max_length=254)
    description = models.TextField()
    has_hours = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024)
    image = models.ImageField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.service
