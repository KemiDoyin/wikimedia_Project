# Generated by Django 4.2.5 on 2023-10-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='report_date',
            field=models.DateTimeField(),
        ),
    ]