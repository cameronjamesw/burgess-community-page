# Generated by Django 4.2.13 on 2025-01-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_staff_member_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_member',
            name='tenure',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
