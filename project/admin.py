from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
from django.utils.safestring import mark_safe

class PageAdmin(admin.ModelAdmin):
    def on_site(self, obj):
        return mark_safe("<a href='%s' target='_blank'>Дивитись на сайті</a>" % obj.get_absolute_url())
    on_site.short_description = "Дивитись на сайті"

    exclude = ['']
    list_display = ['title', 'slug', 'on_site']
    list_display_links = ['title', 'slug']

admin.site.register(Page, PageAdmin)
admin.site.unregister(Group)


admin.site.site_header  = 'Visatut адміністрування'
admin.site.site_title   = 'Visatut адміністрування'
admin.site.index_title  = ''
