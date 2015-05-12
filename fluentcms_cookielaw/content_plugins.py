from django.utils.translation import ugettext_lazy as _
from fluent_contents.extensions import plugin_pool, ContentPlugin
from . import appsettings
from .models import CookieLawItem


@plugin_pool.register
class CookieLawPlugin(ContentPlugin):
    """
    Showing a cookie law notification
    """
    model = CookieLawItem
    category = _("Footer")
    render_template = "fluentcms_cookielaw/banner.html"

    class FrontendMedia:
        js = appsettings.FLUENTCMS_COOKIELAW_JS
        css = appsettings.FLUENTCMS_COOKIELAW_CSS
