from django.contrib import admin
from News.models import Category, SubCategory, Post, Comments
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Name','slug','Posting_date','Update_date']
    prepopulated_fields = {'slug':('Name',)}
    
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['Name','slug']
    prepopulated_fields = {'slug':('Name',)}
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['Title','slug','Posting_date','Update_date']
    prepopulated_fields = {'slug':('Title',)}

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display=['details','Email','Comment_date']
