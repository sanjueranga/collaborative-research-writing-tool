from django.contrib import admin
from .models import UserProfile, Interest, Country,Experience
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "company_name", "country", "job_title", "website")

class InterestAdmin(admin.ModelAdmin):
    list_display = ("id", "label")

class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "label")

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("id", "label")  

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

