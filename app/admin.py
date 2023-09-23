from django.contrib import admin

# Register your models here.
from app.models import *

class customstudent(admin.ModelAdmin):
    list_display=['Sname','Sid','Email']
    list_display_links=['Sid']
    list_editable=['Sname']
    list_per_page=3
    list_filter=['Email']

admin.site.register(Student,customstudent)