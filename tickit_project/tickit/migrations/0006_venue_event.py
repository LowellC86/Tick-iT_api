# Generated by Django 4.0 on 2023-07-20 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0005_venue_venue_url_alter_event_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='event',
            field=models.CharField(default='tbd', max_length=100),
            preserve_default=False,
        ),
    ]
