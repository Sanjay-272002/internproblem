# Generated by Django 3.2 on 2023-01-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_formsss_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formsss',
            name='summary',
            field=models.TextField(max_length=150),
        ),
    ]
