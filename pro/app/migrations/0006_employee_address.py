# Generated by Django 4.2.3 on 2023-08-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_employee_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default=True, max_length=500),
        ),
    ]
