from django.contrib import admin
from .models import TeamMember
from msigana_ecommerce.admin_site import admin_site

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')

admin_site.register(TeamMember, TeamMemberAdmin)