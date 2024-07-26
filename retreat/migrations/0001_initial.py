# Generated by Django 5.0.7 on 2024-07-26 03:48

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Retreat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('duration', models.IntegerField()),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['id', 'date'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('payment_detail', models.CharField(choices=[('PE', 'Pending'), ('SU', 'Successful')], default='Pending', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('retreat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retreat.retreat')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
