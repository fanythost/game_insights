# Generated by Django 2.1 on 2018-11-06 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='of',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Game'),
            preserve_default=False,
        ),
    ]