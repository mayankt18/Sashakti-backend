# Generated by Django 4.0.4 on 2022-05-21 20:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='course',
            field=models.ManyToManyField(blank=True, to='accounts.course'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='job',
            field=models.ManyToManyField(blank=True, to='accounts.job'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='employer',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
