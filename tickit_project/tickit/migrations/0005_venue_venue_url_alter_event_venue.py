# Generated by Django 4.0 on 2023-07-20 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0004_event_tickets_venue_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_url',
            field=models.TextField(default='tbd'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_at_venue', to='tickit.venue'),
        ),
    ]
