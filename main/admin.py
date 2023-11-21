from django.contrib import admin
from main import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']


admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Posts)