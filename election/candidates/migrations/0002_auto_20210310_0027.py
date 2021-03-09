# Generated by Django 2.2.16 on 2021-03-10 00:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='Recommendation_count',
            new_name='recommendation_count',
        ),
        migrations.AddField(
            model_name='candidate',
            name='address',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='available',
            field=models.CharField(blank=True, default='접수', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='career1',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='career2',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='contact',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='pledge',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='candidate',
            name='resident_number',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='signature',
            field=models.FileField(blank=True, null=True, upload_to='uploads/candidates/%Y/%m'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='type',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
    ]
