# Generated by Django 3.0.6 on 2020-05-11 15:05

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('New', 'New'), ('Modal', 'Modal')], max_length=30)),
                ('transaction_status', models.CharField(choices=[('Issued', 'Issued'), ('Pending', 'Pending'), ('In Process', 'In Process')], max_length=30)),
                ('submission_date', models.DateField()),
                ('issuance_date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField()),
            ],
            managers=[
                ('records', django.db.models.manager.Manager()),
            ],
        ),
    ]