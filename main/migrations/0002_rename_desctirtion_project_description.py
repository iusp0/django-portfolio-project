# Generated by Django 4.1.3 on 2022-12-02 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='desctirtion',
            new_name='description',
        ),
    ]