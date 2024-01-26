# Generated by Django 2.0.13 on 2020-09-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200915_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTimeDurationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('voicename', models.CharField(max_length=100)),
                ('timesec', models.IntegerField()),
                ('textlen', models.IntegerField()),
            ],
            options={
                'db_table': 'TimeSecTable',
            },
        ),
    ]
