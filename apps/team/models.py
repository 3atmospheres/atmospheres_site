import os.path
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _

def get_image_path(instance, filename):
    return os.path.join('team', instance.slug, filename)

class Member(models.Model):
    """
    Member Model
    """
    name = models.CharField(_('name'), max_length=200)
    slug = models.SlugField(unique=True)
    enabled = models.BooleanField(default=False)
    sort_order = models.IntegerField(_('sort'), blank=True, null=True)
    title = models.CharField(_('title'), max_length=200)
    bio = models.TextField(_('bio'), blank=True)
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    image = models.ImageField(_(u'image (??x??)'), upload_to=get_image_path, blank=True)

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
        ordering = ('-sort_order',)
        get_latest_by = '-sort_order'

    def __unicode__(self):
        return self.name
