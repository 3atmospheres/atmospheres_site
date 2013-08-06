from datetime import datetime

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.utils.translation import ugettext_lazy as _

from atmospheres_site.apps.team.models import Member

def members(request):
    members = Member.objects.filter(enabled=1).order_by("-sort_order").all()

    return render_to_response("team/team.html", {
        "members": members,
    }, context_instance=RequestContext(request))

