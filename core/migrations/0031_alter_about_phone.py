# Generated by Django 4.2.2 on 2023-10-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_about_delete_aboutdrop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]