# Generated by Django 4.2.2 on 2023-10-27 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_about_degree_about_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='Degree',
            new_name='degree',
        ),
    ]
