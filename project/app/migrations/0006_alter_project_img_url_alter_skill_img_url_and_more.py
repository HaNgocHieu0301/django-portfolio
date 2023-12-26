# Generated by Django 5.0 on 2023-12-25 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img_url',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='img_url',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
