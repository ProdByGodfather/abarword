from django.contrib import admin
from main import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    search_fields = ['title']

class PostsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','date','best']
    list_filter = ['date','best']
    search_fields = ['title','body']

class NewsAdmin(admin.ModelAdmin):
    search_fildes = ['description']

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Posts,PostsAdmin)
admin.site.register(models.News,NewsAdmin)