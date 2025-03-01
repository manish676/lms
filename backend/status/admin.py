from django.contrib import admin
from .models import Status
# Register your models here.


class StatusModel(admin.ModelAdmin):
    list_display = ('title', 'color', 'createdAt')
    
admin.site.register(Status,StatusModel)