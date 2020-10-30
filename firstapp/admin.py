from django.contrib import admin
from .models import results,languages
# Register your models here.
class result(admin.ModelAdmin):
    list_display=('title','answer')
class language(admin.ModelAdmin):
    list_display=('id','language','key')


admin.site.register(results,result)    

admin.site.register(languages,language)   