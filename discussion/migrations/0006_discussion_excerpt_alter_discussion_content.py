# Generated by Django 4.2.13 on 2024-09-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0005_alter_comment_options_alter_discussion_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='excerpt',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
