# Generated by Django 4.2.10 on 2024-02-07 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('legislator', '0001_initial'),
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.bill')),
            ],
            options={
                'db_table': 'vote',
            },
        ),
        migrations.CreateModel(
            name='Vote_Results',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('vote_type', models.IntegerField()),
                ('legislator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislator.legislator')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.vote')),
            ],
            options={
                'db_table': 'vote_results',
            },
        ),
    ]
