# Generated by Django 4.1.7 on 2023-03-10 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_days_weekend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='days',
            old_name='day',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='days',
            new_name='day',
        ),
    ]