# Generated by Django 5.0 on 2024-01-08 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='book',
        ),
    ]
