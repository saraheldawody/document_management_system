# Generated by Django 2.2.13 on 2020-09-09 21:47

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_document_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc',
            field=models.FileField(upload_to=app.models.get_file_path),
        ),
    ]
