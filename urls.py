import os.path
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # static media files
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),

    # index
    (r'^$', 'atmospheres_site.apps.base.views.featured'),

    # work
    (r'^work/', include('atmospheres_site.apps.work.urls')),

    # services
    url(r'services/$', direct_to_template, { "template": "services.html", }, name="services"),

    # contact
    url(r'^contact/', 'atmospheres_site.apps.base.views.contact', name="contact"),
    url(r'thanks/$', direct_to_template, { "template": "thanks.html", }, name="thanks"),

    # team
    (r'team/$', 'atmospheres_site.apps.team.views.members'),

   # about
    url(r'about/$', direct_to_template, { "template": "about.html", }, name="about"),

    # admin
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
