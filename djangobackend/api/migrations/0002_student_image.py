# Generated by Django 3.2.9 on 2022-03-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='none', upload_to='myimage'),
        ),
    ]
