# Generated by Django 4.2.9 on 2024-01-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animalstapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animals',
            name='id',
        ),
        migrations.AlterField(
            model_name='animals',
            name='code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
