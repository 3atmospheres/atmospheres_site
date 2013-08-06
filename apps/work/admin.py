from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from atmospheres_site.apps.work.models import Project, Photo


class ImagesInline(generic.GenericTabularInline):
    model = Photo
    max_num = 10

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'created_at', 'featured')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImagesInline]

admin.site.register(Project, ProjectAdmin)
