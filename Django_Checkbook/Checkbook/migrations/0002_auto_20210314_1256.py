# Generated by Django 3.1.7 on 2021-03-14 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='initical_deposit',
            new_name='initial_deposit',
        ),
    ]
