# Generated by Django 3.1.5 on 2021-05-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
