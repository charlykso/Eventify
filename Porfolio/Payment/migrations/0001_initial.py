# Generated by Django 4.2.1 on 2023-06-08 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('email', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=60)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ticket.ticket')),
            ],
        ),
    ]
