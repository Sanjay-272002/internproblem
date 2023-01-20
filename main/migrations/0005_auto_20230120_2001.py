# Generated by Django 3.2 on 2023-01-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_formss'),
    ]

    operations = [
        migrations.CreateModel(
            name='formsss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_pic/blogimage/')),
                ('catg', models.CharField(choices=[('Mental Health ', 'Mental Health '), ('Heart Disease', 'Heart Disease'), ('Covid', 'Covid'), ('Immunization', 'Immunization')], default='Covid', max_length=50)),
                ('summary', models.TextField(max_length=15)),
                ('content', models.TextField(max_length=300)),
                ('Draft', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='formss',
        ),
    ]