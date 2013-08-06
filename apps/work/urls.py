from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # individual project
    url(r'^(?P<slug>[-\w]+)/$', 'atmospheres_site.apps.work.views.work', name='work'),

    # all projects
    url(r'^$', 'atmospheres_site.apps.work.views.works', name="work_list_all"),
)
