# Generated by Django 2.2 on 2020-01-26 15:58

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banking", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statementfile",
            name="statement_file",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(location="/code/"),
                upload_to="",
            ),
        ),
    ]
