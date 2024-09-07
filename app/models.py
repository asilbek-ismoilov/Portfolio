from django.db import models


class ResumeCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"


class Resume(models.Model):
    date = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    dictionary = models.TextField()
    category = models.ForeignKey(ResumeCategory,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.company})"
    

class WorkCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"


class Work(models.Model):
    image = models.ImageField(upload_to='Images/blog')
    image = models.CharField(max_length=50)
    category = models.ForeignKey(WorkCategory,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.category})"
    

class Blog(models.Model):
    image = models.ImageField(upload_to='Images/blog')
    created_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    content = models.TextField() 

    def __str__(self):
        return f"{self.title} ({self.created_date})"

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"
    