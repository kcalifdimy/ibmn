# Generated by Django 3.2.12 on 2022-04-29 16:52

from django.db import migrations, models
import imagekit.models.fields

import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breaking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(default='text', max_length=300)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='profile_image')),

            ],
        ),
    ]
