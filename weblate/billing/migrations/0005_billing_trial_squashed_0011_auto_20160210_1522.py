# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('billing', '0005_billing_trial'), ('billing', '0006_auto_20160106_1834'), ('billing', '0007_invoice'), ('billing', '0008_billing_state'), ('billing', '0009_remove_billing_trial'), ('billing', '0010_auto_20160210_1407'), ('billing', '0011_auto_20160210_1522')]

    dependencies = [
        ('billing', '0004_auto_20150917_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='trial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plan',
            name='display_limit_languages',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='display_limit_projects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='display_limit_repositories',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plan',
            name='display_limit_strings',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('payment', models.FloatField()),
                ('currency', models.IntegerField(choices=[(0, 'EUR'), (1, 'mBTC')], default=0)),
                ('ref', models.CharField(blank=True, max_length=50)),
                ('note', models.TextField(blank=True)),
                ('billing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Billing')),
            ],
        ),
        migrations.AddField(
            model_name='billing',
            name='state',
            field=models.IntegerField(choices=[(0, 'Active'), (1, 'Trial'), (2, 'Expired')], default=0),
        ),
        migrations.RemoveField(
            model_name='billing',
            name='trial',
        ),
    ]
