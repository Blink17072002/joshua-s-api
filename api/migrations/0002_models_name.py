# Generated by Django 4.2.7 on 2023-11-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
