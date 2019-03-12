# Generated by Django 2.1.7 on 2019-03-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190310_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='subheader',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='subheader1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='subheader2',
            field=models.TextField(null=True),
        ),
    ]
