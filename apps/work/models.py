import os.path
import uuid
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from imagekit.models import ImageModel


def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('work', filename)

class Project(models.Model):
    """
    Project Model
    """
    name = models.CharField(_('Name'), max_length=200)
    slug = models.SlugField(unique=True)
    enabled = models.BooleanField(default=False)
    url = models.URLField(_('Project URL'), blank=True, null=True)
    tease = models.CharField(_('Tease'), max_length=200, blank=True)
    description = models.TextField(_('Description'), blank=True)
    created_at = models.DateTimeField(_('Created at'), default=datetime.now)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    thumbnail = models.ImageField(_(u'Thumbnail (250x130)'), upload_to=get_image_path)
    images = generic.GenericRelation('Photo', blank=True, null=True)
    featured = models.BooleanField(_(u"Featured on homepage?"), default=False)
    featured_image = models.ImageField(_(u'Featured Image (900x250)'), upload_to=get_image_path, blank=True, null=True)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ('-created_at',)
        get_latest_by = 'created_at'

    def __unicode__(self):
        return self.name

class Photo(ImageModel):
    name = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to=get_image_path)
    num_views = models.PositiveIntegerField(editable=False, default=0)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class IKOptions:
        spec_module         = 'apps.work.specs'
        cache_dir           = 'work'
        image_field         = 'original_image'
        save_count_as       = 'num_views'

