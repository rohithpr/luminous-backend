from django.contrib import admin
from .models import User, Location, LocationUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ('resources', )

class LocationAdmin(admin.ModelAdmin):
    fields = ('left_top', 'resources')

class LocationUserAdmin(admin.ModelAdmin):
    fields = ('user', 'location')

admin.site.register(User, UserAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(LocationUser, LocationUserAdmin)
