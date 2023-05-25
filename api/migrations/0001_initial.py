# Generated by Django 4.2.1 on 2023-05-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioElement',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('vo', 'Voice Over'), ('bg_music', 'Background Music'), ('video_music', 'Video Music')], max_length=20)),
                ('video_component_id', models.CharField(blank=True, max_length=255, null=True)),
                ('high_volume', models.IntegerField()),
                ('low_volume', models.IntegerField()),
                ('duration_start_time', models.IntegerField(blank=True, null=True)),
                ('duration_end_time', models.IntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AudioFragments',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('url', models.URLField(blank=True, null=True)),
                ('type', models.CharField(max_length=20)),
                ('volume', models.IntegerField()),
                ('duration_start_time', models.IntegerField()),
                ('duration_end_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoElement',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('audio_id', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('duration_start_time', models.IntegerField()),
                ('duration_end_time', models.IntegerField()),
            ],
        ),
    ]
