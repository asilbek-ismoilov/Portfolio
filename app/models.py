from django.db import models
from django.utils.text import slugify

class Experience(models.Model):
    date = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    dictionary = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.company})"
    
class Education(models.Model):
    date = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    dictionary = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.company})"
    

class WorkCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"


class Work(models.Model):
    image = models.ImageField(upload_to='Images/work')
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.name} ({self.category})"
    

class Blog(models.Model):
    image = models.ImageField(upload_to='Images/blog')
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=150)
    content = models.TextField() 
    slug = models.SlugField(unique=True, blank=True) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.date})"

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"
