# Generated by Django 3.2.12 on 2022-05-20 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='level',
        ),
        migrations.RemoveField(
            model_name='category',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tree_id',
        ),
    ]
