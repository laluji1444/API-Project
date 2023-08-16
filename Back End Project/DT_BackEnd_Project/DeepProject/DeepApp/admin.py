from django.contrib import admin
from DeepApp.models import Name

# Register your models here.
class NameAdmin(admin.ModelAdmin):
    
    list_display = ['name','image','tagline','schedule','description','moderator','category','sub_category','rigor_rank']

admin.site.register(Name,NameAdmin)
