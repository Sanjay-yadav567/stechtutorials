from django.contrib import admin
from .models import Category, Post

# Register your models here.

#for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','descripition','url')
    search_fields =('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','url','add_date')
    search_fields =('title',)
    list_filter = ('cat',)
    list_per_page = 20



admin.site.register(Category,CategoryAdmin)

admin.site.register(Post,PostAdmin)

