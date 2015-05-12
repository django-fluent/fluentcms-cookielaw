from django.conf import settings

_default_js = ('fluentcms_cookielaw/js/cookielaw.js',)

# Allow overriding the complete FrontendMedia definition
FLUENTCMS_COOKIELAW_JS = getattr(settings, 'FLUENTCMS_COOKIELAW_JS', _default_js)
FLUENTCMS_COOKIELAW_CSS = getattr(settings, 'FLUENTCMS_COOKIELAW_CSS', {})
