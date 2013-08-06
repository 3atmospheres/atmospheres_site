from datetime import datetime

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.utils.translation import ugettext_lazy as _

from atmospheres_site.apps.work.models import Project

def works(request):
    works = Project.objects.filter(enabled=1).order_by("-created_at").all()

    return render_to_response("work/works.html", {
        "works": works,
    }, context_instance=RequestContext(request))

def work(request, slug):
    works = Project.objects.filter(enabled=1).all()
    work = get_object_or_404(works, slug=slug)

    return render_to_response("work/work.html", {
        "work": work,
    }, context_instance=RequestContext(request))
