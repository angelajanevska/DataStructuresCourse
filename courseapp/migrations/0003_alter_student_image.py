# Generated by Django 4.0.6 on 2022-08-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]