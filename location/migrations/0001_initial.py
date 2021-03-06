# Generated by Django 3.0.6 on 2020-05-11 15:05

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'branch',
                'verbose_name_plural': 'branches',
            },
            managers=[
                ('locations', django.db.models.manager.Manager()),
            ],
        ),
    ]
