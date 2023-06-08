# Generated by Django 4.2.1 on 2023-06-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('Con', 'Concert'), ('Com', 'Communities'), ('Cl', 'Classes'), ('P', 'Parties'), ('S', 'Sport')], default='Event', max_length=60),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('Con', 'Concert'), ('Com', 'Communities'), ('Cl', 'Classes'), ('P', 'Parties'), ('S', 'Sport')], default='Event', max_length=60),
        ),
    ]
