# Generated by Django 3.2.14 on 2022-08-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='link_to_git',
            field=models.URLField(blank=True, null=True, verbose_name='Link to git'),
        ),
    ]
