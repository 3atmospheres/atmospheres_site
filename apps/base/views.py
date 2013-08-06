from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from atmospheres_site.apps.work.models import Project
from atmospheres_site.apps.base.forms import ContactForm


def featured(request):
    works = Project.objects.filter(enabled=1,featured=1).order_by("-created_at").all()

    return render_to_response("home.html", {
        "works": works,
    }, context_instance=RequestContext(request))


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()

            # build the message
            content = 'Name: ' + name + '\n\nEmail: ' + email + '\n\nMessage: ' + message
            recipient = ['hello@3atmospheres.com']

            send_mail(subject, content, email, recipient)

            return HttpResponseRedirect("/thanks/")
    else:
        form = ContactForm()

    return render_to_response("contact.html", {
        "form": form,
    }, context_instance=RequestContext(request))
