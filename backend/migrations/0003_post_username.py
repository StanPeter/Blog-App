# Generated by Django 3.1.2 on 2020-10-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20201019_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]