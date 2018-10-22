from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from cms.models import CMSPlugin


class NonStrippingTextField(models.TextField):
    """A TextField that does not strip whitespace at the beginning/end of
    it's value.  Might be important for markup/code."""

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super().formfield(**kwargs)


class NonStrippingCharField(models.CharField):
    """A CharField that does not strip whitespace at the beginning/end of
    it's value.  Might be important for markup/code."""

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super().formfield(**kwargs)


@python_2_unicode_compatible
class CMSCharFieldPlugin(CMSPlugin):
    body = NonStrippingCharField(_('body'), max_length=500)

    def __str__(self):
        return self.body

    search_fields = ('body',)


@python_2_unicode_compatible
class CMSTextFieldPlugin(CMSPlugin):
    body = NonStrippingTextField(_('body'))

    def __str__(self):
        return self.body

    search_fields = ('body',)

