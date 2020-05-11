# Generated by Django 3.0.6 on 2020-05-11 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branch_head',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_manager': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branch', to='user.SalesPerson'),
        ),
    ]
