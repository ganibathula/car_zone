from django.contrib import admin
from .models import car_model
from django.utils.html import format_html
# Register your models here.
class car_model_admin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html("<img src='{}' width='40px' style='border-radius:50px;'/>".format(object.car_photo.url))
    thumbnail.short_description='car Image'
    list_display = ['id','car_title','color','thumbnail','model','year','body_style','fuel_type','is_featured']
    list_editable = ['is_featured']
    list_display_links = ['id','car_title','thumbnail']
    search_fields = ['id','car_title','city','fuel_type','body_style','year']

admin.site.register(car_model,car_model_admin)