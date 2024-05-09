from django.db import models

class Slide(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    def __str__(self):
        return f"Slide {self.id}"

class HomeSection(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slides = models.ManyToManyField(Slide)
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images_livres/')
    def __str__(self):
        return self.title

class Noveltie(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='novelty_images/')
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='announcement_images/')
    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)  
    content = models.TextField()    
    def get_stars(self):
        return range(1, self.rating + 1)
    def __str__(self):
        return self.author

