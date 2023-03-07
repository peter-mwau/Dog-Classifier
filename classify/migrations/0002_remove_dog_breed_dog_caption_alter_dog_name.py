# Generated by Django 4.1.7 on 2023-03-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='breed',
        ),
        migrations.AddField(
            model_name='dog',
            name='caption',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
