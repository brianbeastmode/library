# Generated by Django 3.1.3 on 2020-11-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20201122_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bookImage',
            field=models.ImageField(blank=True, upload_to='covers'),
        ),
    ]
