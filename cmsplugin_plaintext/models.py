from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from cms.models import CMSPlugin


@python_2_unicode_compatible
class CMSCharFieldPlugin(CMSPlugin):
    body = models.CharField(_('body'), max_length=500, strip=False)

    def __str__(self):
        return self.body

    search_fields = ('body',)


@python_2_unicode_compatible
class CMSTextFieldPlugin(CMSPlugin):
    body = models.TextField(_('body'), strip=False)

    def __str__(self):
        return self.body

    search_fields = ('body',)

