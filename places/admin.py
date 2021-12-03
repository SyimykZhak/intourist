from django.contrib import admin
from .models import Feedback, Place
# Register your models here.

admin.site.register(Place)


class FeedbackAdmin(admin.ModelAdmin):
    list_display =[ 'text','place','user','checked'] #порядок
    list_editable = ['user','checked'] #для того чтобы редактировать
    list_filter = ['checked'] #фильтр
    search_fields = ['text','place__name','place__location','place_description']  #поиск


    fields = ['user','place','text'] #оставить только эти
    readonly_fields = ['place','text'] #те поля которые только на чтение

admin.site.register(Feedback,FeedbackAdmin)