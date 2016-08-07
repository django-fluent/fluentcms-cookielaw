.. image:: https://img.shields.io/travis/edoburu/fluentcms-cookielaw/master.svg?branch=master
    :target: http://travis-ci.org/edoburu/fluentcms-cookielaw
.. image:: https://img.shields.io/pypi/v/fluentcms-cookielaw.svg
    :target: https://pypi.python.org/pypi/fluentcms-cookielaw/
.. image:: https://img.shields.io/pypi/l/fluentcms-cookielaw.svg
    :target: https://pypi.python.org/pypi/fluentcms-cookielaw/
.. image:: https://img.shields.io/codecov/c/github/edoburu/fluentcms-cookielaw/master.svg
    :target: https://codecov.io/github/edoburu/fluentcms-cookielaw?branch=master

fluentcms-cookielaw
===================

A plugin for django-fluent-contents_ to show a cookie notification on a website.

Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI::

    pip install fluentcms-cookielaw


Backend Configuration
---------------------

First make sure the project is configured for django-fluent-contents_.

Then add the following settings::

    INSTALLED_APPS += (
        'fluentcms_cookielaw',
    )

The database tables can be created afterwards::

    ./manage.py syncdb

Now, the ``CookieLawPlugin`` can be added to your ``PlaceholderField``
and ``PlaceholderEditorAdmin`` admin screens.


Frontend Configuration
----------------------

Make sure that all plugin media files are exposed by django-fluent-contents_::

    {% load fluent_contents_tags %}

    {% render_content_items_media %}

This tag should be placed at the bottom of the page, after all plugins are rendered.
For more configuration options - e.g. integration with django-compressor -
see the `template tag documentation <https://django-fluent-contents.readthedocs.io/en/latest/templatetags.html#frontend-media>`_.

CSS Code
~~~~~~~~

The stylesheet code is purposefully left out, since authors typically like to provide their own styling.

To get started quickly, include ``fluentcms_cookielaw/js/cookielaw.css`` in your site.

JavaScript Code
~~~~~~~~~~~~~~~

No configuration is required for the JavaScript integration.

By default, the plugin includes all required JavaScript code to hide the cookie notification bar.

If needed, the includes resources can be changed by using the following settings::

    FLUENTCMS_COOKIELAW_JS = (
        'fluentcms_cookielaw/js/cookielaw.js',
    )

If a value is defined as ``None``, it will be excluded from the frontend media.

HTML code
~~~~~~~~~

If needed, the HTML code can be overwritten by redefining ``fluentcms_cookielaw/banner.html``.

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/django-fluent/django-fluent-contents
