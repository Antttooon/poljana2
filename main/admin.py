from django.contrib import admin
from .models import *

# Register your models here.


# Модель категории

class BGAdmin(admin.ModelAdmin):
    list_display = ['id','image_img','created','display']
    list_editable = ['display']
    ordering = ['id']



class AlboomAdmin(admin.ModelAdmin):
    list_display = ['image_img','name', 'slug','display']
    #prepopulated_fields = {'slug': ('name',)}
    list_editable = ['display']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['image_img','name','created']
    list_filter = ['created']
    list_editable = []
    prepopulated_fields = {'slug': ('name', )}


class MusicianAdmin(admin.ModelAdmin):
    list_display = ['name', 'm_photo','display']
    list_editable = ['display']

class MainTextAdmin(admin.ModelAdmin):
    list_display = ['text_header','main_text','display']
    list_editable = ['display']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['header','body','display']
    list_editable = ['body','display']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['header','body','display']
    list_editable = ['body','display']

class AfishaAdmin(admin.ModelAdmin):
    list_display = ['header1','header2','header3','header4','header5','display']
    list_editable = ['display']
    ordering = ['created']




#class AudioAdmin(admin.ModelAdmin):
 #   list_display = ['author','alboom','name','audio_file','created','updated']
  #  list_editable = ['alboom','name']




admin.site.register(BG_image,BGAdmin)
admin.site.register(Photo_Alboom, AlboomAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Musician,MusicianAdmin)
admin.site.register(MainText,MainTextAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Afisha,AfishaAdmin)
#admin.site.register(Audio,AudioAdmin)