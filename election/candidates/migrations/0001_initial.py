# Generated by Django 2.2.13 on 2021-03-01 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=64)),
                ('Recommendation_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(default='')),
                ('recommender', models.CharField(max_length=64)),
                ('contact', models.CharField(max_length=64)),
                ('signature', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate')),
            ],
        ),
    ]
