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

class ContactAdmin(admin.ModelAdmin):
    search_fields = ['email','name','message']
    list_display = ['email','name']

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Posts,PostsAdmin)
admin.site.register(models.News,NewsAdmin)
admin.site.register(models.Contact,ContactAdmin)
admin.site.register(models.Emails)