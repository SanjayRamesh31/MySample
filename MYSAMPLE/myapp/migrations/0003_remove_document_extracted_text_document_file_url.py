# Generated by Django 5.0.7 on 2024-07-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_document_extracted_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='extracted_text',
        ),
        migrations.AddField(
            model_name='document',
            name='file_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
