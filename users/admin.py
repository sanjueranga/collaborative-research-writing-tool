from django.contrib import admin
from .models import UserProfile,Interest,Country


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user","time_stamp")

class InterestAdmin(admin.ModelAdmin):
    list_display = ("id", "label")
    
class CountryAdmin(admin.ModelAdmin):
     list_display = ("id", "label")


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Country, CountryAdmin)

