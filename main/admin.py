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


admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Posts,PostsAdmin)