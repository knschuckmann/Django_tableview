from django.contrib import admin

from .models import Webapp
# Register your models here.
@admin.register(Webapp)
class DeviceAdmin(admin.ModelAdmin):
    search_fields =['id', 'timestamp', 'duration']
    list_display = ('id', 'timestamp', 'temperature', 'duration')
    list_filter = ()