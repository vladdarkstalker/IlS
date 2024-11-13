# Generated by Django 5.1.3 on 2024-11-12 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnsys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PsychQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('factor', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PsychTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('form', models.CharField(choices=[('A', 'Form A'), ('B', 'Form B')], max_length=1)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PsychAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('score', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='learnsys.psychquestion')),
            ],
        ),
        migrations.AddField(
            model_name='psychquestion',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='learnsys.psychtest'),
        ),
        migrations.CreateModel(
            name='PsychTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor', models.CharField(max_length=2)),
                ('result', models.FloatField()),
                ('date_taken', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='learnsys.psychtest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
