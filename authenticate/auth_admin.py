from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    # # Cria um filtro de hierarquia com datas
    # search_fields = ('user__username',)
    # readonly_fields = ('user',)
    # list_display = ('user','birthday', 'address', 'city', 'state')
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow)
