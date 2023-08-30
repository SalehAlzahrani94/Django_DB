# Generated by Django 4.2.4 on 2023-08-28 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('passwd', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ACTOR', 'Actor'), ('DIRECTOR', 'director')], max_length=20, verbose_name='the role this member had in this movie ')),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.members')),
            ],
        ),
        migrations.CreateModel(
            name='movies_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the movie', max_length=50)),
                ('date', models.CharField(help_text='date the movie was relased ', max_length=50)),
                ('members', models.ManyToManyField(through='website.MovieMembers', to='website.members')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the publisher', max_length=50)),
                ('website', models.URLField(help_text='pubisher website', max_length=100)),
                ('email', models.EmailField(help_text='pubisher website', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='the reivew text', max_length=100)),
                ('rating', models.IntegerField(help_text='the rating the reivew given ')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='the time and date reivew was created ')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(help_text='this line if you delete move delete his reviews ', on_delete=django.db.models.deletion.CASCADE, to='website.movies_info')),
            ],
        ),
        migrations.AddField(
            model_name='movies_info',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.publisher'),
        ),
        migrations.AddField(
            model_name='moviemembers',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.movies_info'),
        ),
    ]