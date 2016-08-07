from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _
from fluent_contents.extensions import PluginHtmlField
from fluent_contents.models import ContentItem


@python_2_unicode_compatible
class CookieLawItem(ContentItem):
    """
    Cookie law item
    """
    text = PluginHtmlField(_("Text"), help_text=_("For example: 'We use cookies to ensure you get the best experience on our website'"))
    button_text = models.CharField(_("Button text"), max_length=100)  # e.g. "Close" or "Accept"

    class Meta:
        verbose_name = _("Cookie notification")
        verbose_name_plural = _("Cookie notifications")

    def __str__(self):
        return Truncator(strip_tags(self.text)).words(20)
