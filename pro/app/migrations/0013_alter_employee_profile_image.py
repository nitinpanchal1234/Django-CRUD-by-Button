# Generated by Django 4.2.2 on 2023-08-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_age_employee_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_image',
            field=models.ImageField(default=None, null=True, upload_to='media/'),
        ),
    ]
