# Generated by Django 2.2.7 on 2020-11-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_actors', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Overview_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('release_date', models.CharField(max_length=30, null=True)),
                ('runningtime', models.CharField(max_length=10, null=True)),
                ('rating', models.TextField()),
                ('nation', models.CharField(max_length=255, null=True)),
                ('maker', models.CharField(max_length=255, null=True)),
                ('director', models.CharField(max_length=255, null=True)),
                ('actors', models.ManyToManyField(blank=True, related_name='movie_casts', to='movies.Movie_cast')),
                ('genres', models.ManyToManyField(related_name='movie_genre', to='movies.Genre')),
                ('overview_tags', models.ManyToManyField(null=True, related_name='overview_tags', to='movies.Overview_tag')),
            ],
        ),
    ]
