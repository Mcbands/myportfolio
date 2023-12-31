# Generated by Django 4.2.2 on 2023-10-27 14:27

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_portfolio_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
