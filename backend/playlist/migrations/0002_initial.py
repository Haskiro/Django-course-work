# Generated by Django 4.0.5 on 2022-06-20 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('track', '0001_initial'),
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='tracks',
            field=models.ManyToManyField(related_name='playlists', to='track.track', verbose_name='Треки'),
        ),
    ]
