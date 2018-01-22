# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fluent_contents.extensions


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieLawItem',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem', on_delete=models.CASCADE)),
                ('text', fluent_contents.extensions.PluginHtmlField(help_text="For example: 'We use cookies to ensure you get the best experience on our website'", verbose_name='Text')),
                ('button_text', models.CharField(max_length=100, verbose_name='Button text')),
            ],
            options={
                'db_table': 'contentitem_fluentcms_cookielaw_cookielawitem',
                'verbose_name': 'Cookie notification',
                'verbose_name_plural': 'Cookie notifications',
            },
            bases=('fluent_contents.contentitem',),
        ),
    ]
