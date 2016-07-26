from django.contrib import admin
from .models import Page
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    '''
        Admin View for Page
    '''
    fieldsets = (
        (None, {
            'fields': ( 'title', 'description', 'pub_date')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )


admin.site.register(Page, PageAdmin)