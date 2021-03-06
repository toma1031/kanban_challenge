# Generated by Django 2.2.17 on 2021-05-13 01:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicketCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('post_person', models.CharField(default='John Due', max_length=20, verbose_name='PostPerson')),
                ('content', models.TextField(verbose_name='Contents')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
            ],
        ),
    ]
