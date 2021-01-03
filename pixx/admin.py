from django.contrib import admin
from .models import *
import admin_thumbnails

class PixxxAdmin(admin.ModelAdmin):
    model = Pixxx
    list_display = ['image','image_tag']


admin.site.register(Pixxx,PixxxAdmin)

# Register your models here.
