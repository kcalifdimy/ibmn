# Generated by Django 3.2.12 on 2022-05-20 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20220520_1400'),
        ('trending', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trending',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
    ]
