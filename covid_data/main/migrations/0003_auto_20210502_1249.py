# Generated by Django 3.2 on 2021-05-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210502_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='world',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='world',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='area',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='country',
            name='world',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
