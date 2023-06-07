# Generated by Django 4.2.1 on 2023-05-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventify', '0002_remove_events_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='type',
            field=models.CharField(choices=[('P', 'Party'), ('E', 'Event'), ('S', 'Show')], default='Event', max_length=60),
        ),
    ]