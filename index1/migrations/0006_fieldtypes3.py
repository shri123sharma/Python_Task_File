# Generated by Django 4.0.5 on 2022-07-06 13:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('index1', '0005_fieldtypes2_post_choics'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldTypes3',
            fields=[
                ('time', models.TimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('small', models.FloatField(max_length=100)),
                ('slug', models.SlugField(default=True, help_text='this text is name with add(_)', max_length=100)),
                ('duration', models.DurationField()),
            ],
        ),
    ]
