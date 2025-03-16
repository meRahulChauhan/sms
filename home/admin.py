from django.contrib import admin
from .models import Choice, Newsletter

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('__str__',)  # Customize as needed
    search_fields = ('__str__',)  # Customize as needed

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'time')
    search_fields = ('name', 'email')
    list_filter = ('time',)

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
