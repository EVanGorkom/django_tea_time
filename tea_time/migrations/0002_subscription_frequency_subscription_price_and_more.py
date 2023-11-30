# Generated by Django 4.2.7 on 2023-11-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea_time', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='frequency',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='tea',
            name='brew_time',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='tea',
            name='temperature',
            field=models.IntegerField(default=185),
        ),
    ]