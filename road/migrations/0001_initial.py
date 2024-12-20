# Generated by Django 5.1.2 on 2024-10-30 15:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('body', models.TextField()),
                ('publicare', models.DateTimeField(default=django.utils.timezone.now)),
                ('creare', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
