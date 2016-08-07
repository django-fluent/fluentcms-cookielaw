from django.test import TestCase
from fluent_contents.tests.factories import create_content_item
from fluent_contents.tests.utils import render_content_items
from fluentcms_cookielaw.models import CookieLawItem


class CookieLawTests(TestCase):
    """
    Testing private notes
    """

    def test_rendering(self):
        """
        Test the standard button
        """
        item = create_content_item(CookieLawItem, text="Do you like cookies?", button_text="Jummie!")
        output = render_content_items([item])

        self.assertHTMLEqual(output.html,
                             '''<div id="cookielaw-banner">
                                    <div class="container">
                                        <a class="btn" href="javascript:Cookielaw.accept();">Jummie!</a>
                                        Do you like cookies?
                                    </div>
                                </div>''')
        self.assertHTMLEqual(str(output.media), '<script type="text/javascript" src="/static/fluentcms_cookielaw/js/cookielaw.js"></script>')

        self.assertEqual(str(item), 'Do you like cookies?')
