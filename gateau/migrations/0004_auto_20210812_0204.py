# Generated by Django 3.2.6 on 2021-08-11 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gateau', '0003_alter_dessert_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='cafe',
        ),
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gateau.dessert'),
            preserve_default=False,
        ),
    ]
