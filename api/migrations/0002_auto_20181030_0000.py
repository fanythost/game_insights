# Generated by Django 2.1 on 2018-10-30 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(blank=True, to='api.Genre'),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(max_length=50, verbose_name='The Publisher of the game'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='members',
            field=models.ManyToManyField(blank=True, to='api.Game'),
        ),
    ]
