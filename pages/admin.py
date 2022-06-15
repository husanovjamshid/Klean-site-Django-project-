from django.contrib import admin
from .models import Post, Comment, Category, Contact, CategoryImg, PostImg
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','cat_id', 'date', 'view_count')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(CategoryImg)
admin.site.register(PostImg)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date')
admin.site.register(Contact, ContactAdmin)
