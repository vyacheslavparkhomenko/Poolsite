# Generated by Django 2.2.6 on 2019-10-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infpoolsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='picture',
        ),
    ]
