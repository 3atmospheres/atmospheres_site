from django.contrib import admin
from atmospheres_site.apps.team.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at', 'enabled')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Member, MemberAdmin)
