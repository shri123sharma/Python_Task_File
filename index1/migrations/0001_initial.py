# Generated by Django 4.0.5 on 2022-07-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestFieldType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bool', models.BooleanField(default=True)),
                ('char', models.CharField(help_text='Only For Name', max_length=200, unique=True, verbose_name='new_name')),
                ('date', models.DateField(auto_now=True)),
                ('decimal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('email', models.EmailField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
