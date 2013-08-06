from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Contact(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(default=datetime.now, editable=False)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

