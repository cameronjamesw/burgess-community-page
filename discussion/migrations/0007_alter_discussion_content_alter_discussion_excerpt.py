# Generated by Django 4.2.13 on 2024-09-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0006_discussion_excerpt_alter_discussion_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='excerpt',
            field=models.CharField(max_length=100),
        ),
    ]
