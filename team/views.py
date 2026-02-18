# team/views.py

from django.shortcuts import render
from .models import TeamMember

def team_list(request):
    members = TeamMember.objects.all()
    return render(request, 'team_list.html', {'members': members})
