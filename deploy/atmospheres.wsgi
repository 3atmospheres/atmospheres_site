import os
import sys

sys.path.append('/path/to/your/site/goes/here/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'atmospheres_site.settings'

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
