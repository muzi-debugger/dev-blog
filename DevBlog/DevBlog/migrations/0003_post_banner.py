# Generated by Django 5.1.4 on 2025-01-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DevBlog', '0002_remove_post_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
