# Generated by Django 3.2.12 on 2022-05-22 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bignews', '0002_rename_category_name_bignews_category'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=300, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('bignews', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bignews_comments', to='bignews.bignews')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.news')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='comments.comment')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
