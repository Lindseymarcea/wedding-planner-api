# Generated by Django 4.1.5 on 2023-02-05 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0004_song_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('link', models.URLField()),
                ('bought', models.BooleanField()),
                ('guestlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registry.guestlist')),
            ],
        ),
    ]
