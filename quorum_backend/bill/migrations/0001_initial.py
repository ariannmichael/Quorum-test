# Generated by Django 4.2.10 on 2024-02-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('primary_sponsor', models.IntegerField()),
            ],
        ),
    ]
