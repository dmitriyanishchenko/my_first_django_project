# Generated by Django 2.2.1 on 2019-05-29 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(default=None, max_length=255)),
                ('year_of_issue', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MusicBand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_band_name', models.CharField(default=None, max_length=255)),
                ('year_of_foundation', models.PositiveSmallIntegerField()),
                ('music_style', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(default=None, max_length=255)),
                ('track_duration', models.CharField(default=None, max_length=255)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='track', to='hw_21.Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='music_band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album', to='hw_21.MusicBand'),
        ),
    ]
