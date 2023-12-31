# Generated by Django 3.2 on 2022-10-22 15:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import psqlextra.indexes.unique_index
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Title')),
                ('description', models.TextField(default='', null=True, verbose_name='Description')),
                ('creation_date', models.DateField(default='', null=True, verbose_name='Creation Date')),
                ('file_path', models.FileField(blank=True, null=True, upload_to='film_works/', verbose_name='FilePath')),
                ('rating', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Rating')),
                ('type', models.CharField(choices=[('movie', 'Movie'), ('TV_show', 'TV_show')], default='movie', max_length=25, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Filmwork',
                'verbose_name_plural': 'Filmworks',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Name')),
                ('description', models.TextField(default='', null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('full_name', models.CharField(default='', max_length=255, verbose_name='Full Name')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('role', models.TextField(default='', null=True, verbose_name='Role')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('film_work_id', models.ForeignKey(db_column='film_work_id', on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='Filmwork')),
                ('person_id', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='movies.person', verbose_name='Person')),
            ],
            options={
                'verbose_name': 'PersonFilmwork',
                'verbose_name_plural': 'PersonFilmworks',
                'db_table': 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('film_work_id', models.ForeignKey(db_column='film_work_id', on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='Filmwork')),
                ('genre_id', models.ForeignKey(db_column='genre_id', on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'GenreFilmwork',
                'verbose_name_plural': 'GenreFilmworks',
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmwork', to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persones',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.Person'),
        ),
        migrations.AddIndex(
            model_name='personfilmwork',
            index=psqlextra.indexes.unique_index.UniqueIndex(fields=['film_work_id', 'person_id', 'role'], name='person_film_film_wo_6b9cac_idx'),
        ),
        migrations.AddIndex(
            model_name='genrefilmwork',
            index=psqlextra.indexes.unique_index.UniqueIndex(fields=['film_work_id', 'genre_id'], name='genre_film__film_wo_399489_idx'),
        ),
    ]
