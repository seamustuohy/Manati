#
# Copyright (c) 2017 Stratosphere Laboratory.
# 
# This file is part of ManaTI Project 
# (see <https://stratosphereips.org>). It was created by 'Raul B. Netto <raulbeni@gmail.com>'
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. See the file 'docs/LICENSE' or see <http://www.gnu.org/licenses/> 
# for copying permission.
#
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-23 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manati_ui', '0004_auto_20160921_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='weblog',
            name='attributes',
            field=jsonfield.fields.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='weblog',
            name='mod_attributes',
            field=jsonfield.fields.JSONField(default='', null=True),
        ),
        migrations.RemoveField(
            model_name='analysissession',
            name='created_at',
        ),
        migrations.AddField(
            model_name='analysissession',
            name='created_at',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                      verbose_name='created_at'),
        ),
        migrations.RemoveField(
            model_name='analysissession',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='analysissession',
            name='updated_at',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                           verbose_name='updated_at'),
        ),
        migrations.RunSQL("DROP TABLE IF EXISTS manati_analysis_sessions_users;"),
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE',
                          reverse_sql=migrations.RunSQL.noop),
        migrations.CreateModel(
            name='AnalysisSessionUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('columns_order', jsonfield.fields.JSONField(default='', null=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'manati_analysis_sessions_users'
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('object_id', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=255)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'manati_comments',
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('event_name', models.CharField(max_length=30)),
                ('params', jsonfield.fields.JSONField(default='', null=True)),
                ('object_id', models.CharField(max_length=20)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'manati_metrics',
            },
        ),
        migrations.CreateModel(
            name='WeblogHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('new_verdict', models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('false_positive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('false_positive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('false_positive_malicious', 'False Positive/Malicious'), ('false_positive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_false_positive', 'Undefined/False Positive')], default='undefined', max_length=20)),
                ('old_verdict', models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('false_positive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('false_positive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('false_positive_malicious', 'False Positive/Malicious'), ('false_positive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_false_positive', 'Undefined/False Positive')], default='undefined', max_length=20)),
                ('description', models.CharField(max_length=255, null=True)),
                ('object_id', models.CharField(max_length=20)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'manati_weblog_history',
            },
        ),
        migrations.RemoveField(
            model_name='weblog',
            name='created_at',
        ),
        migrations.AddField(
            model_name='weblog',
            name='created_at',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False,
                                                      verbose_name='created_at'),
        ),
        migrations.RemoveField(
            model_name='weblog',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='weblog',
            name='updated_at',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False,
                                                           verbose_name='updated_at'),
        ),
        migrations.AlterField(
            model_name='weblog',
            name='verdict',
            field=models.CharField(
                choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'),
                         ('undefined', 'Undefined'), ('false_positive', 'False Positive'),
                         ('malicious_legitimate', 'Malicious/Legitimate'),
                         ('suspicious_legitimate', 'Suspicious/Legitimate'),
                         ('undefined_legitimate', 'Undefined/Legitimate'),
                         ('false_positive_legitimate', 'False Positive/Legitimate'),
                         ('undefined_malicious', 'Undefined/Malicious'),
                         ('suspicious_malicious', 'Suspicious/Malicious'),
                         ('false_positive_malicious', 'False Positive/Malicious'),
                         ('false_positive_suspicious', 'False Positive/Suspicious'),
                         ('undefined_suspicious', 'Undefined/Suspicious'),
                         ('undefined_false_positive', 'Undefined/False Positive')], default='undefined', max_length=20,
                null=True),
        ),
        migrations.AlterField(
            model_name='analysissessionusers',
            name='columns_order',
            field=jsonfield.fields.JSONField(default=b'{}', null=True),
        ),
        migrations.AlterField(
            model_name='weblog',
            name='attributes',
            field=jsonfield.fields.JSONField(default=b'{}'),
        ),
        migrations.AlterField(
            model_name='weblog',
            name='mod_attributes',
            field=jsonfield.fields.JSONField(default=b'{}', null=True),
        ),
        migrations.AddField(
            model_name='webloghistory',
            name='weblog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manati_ui.Weblog'),
        ),
        migrations.AddField(
            model_name='analysissessionusers',
            name='analysis_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manati_ui.AnalysisSession'),
        ),
        migrations.AddField(
            model_name='analysissessionusers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='analysissession',
            name='users',
            field=models.ManyToManyField(through='manati_ui.AnalysisSessionUsers', to=settings.AUTH_USER_MODEL),
        ),
    ]
