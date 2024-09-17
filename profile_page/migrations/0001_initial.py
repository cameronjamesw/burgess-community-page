# Generated by Django 4.2.13 on 2024-09-17 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp', models.IntegerField(choices=[(0, 'Burgess'), (1, 'Hayward')], default=0)),
                ('position', models.CharField(max_length=50)),
                ('tenure', models.IntegerField(default=0)),
                ('facts', models.TextField()),
                ('memory', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
