# Generated by Django 4.2.3 on 2023-07-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0003_event_is_concert_event_is_sports_event_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tickets',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
