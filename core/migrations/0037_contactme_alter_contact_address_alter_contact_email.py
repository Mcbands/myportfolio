# Generated by Django 4.2.2 on 2023-10-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_rename_point_about_point1_remove_about_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact Me',
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
