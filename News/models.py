from django.db import models

# Create your models here.
class Category(models.Model):
    Name=models.CharField(max_length=200)
    Description=models.CharField(max_length=1000)
    Update_date=models.DateTimeField(auto_now = True)
    Posting_date=models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(max_length=200,unique=True)
    IsActive=models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name
    
class SubCategory(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE) 
    description=models.CharField(max_length=1000)
    Name=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    IsActive=models.BooleanField(default=True)

    def __str__(self):
        return self.Name

class Post(models.Model):
    Title=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    Description=models.CharField(max_length=1000)
    Update_date=models.DateTimeField(auto_now = True)
    Posting_date=models.DateTimeField(auto_now_add = True)
    Image= models.ImageField(upload_to='post/%Y/%m/%d',blank = True)
    slug = models.SlugField(max_length=200,unique=True)
    IsActive=models.BooleanField(default=True)
    
    def __str__(self):
        return self.Title
    
    
class Comments(models.Model):
    Comment_date=models.DateTimeField(auto_now = True)
    details=models.CharField(max_length=1000)
    Fullname=models.CharField(max_length=500)
    Email=models.CharField(max_length=300)
    
    def __str__(self):
        return self.details
    
    

