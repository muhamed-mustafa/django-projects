# Generated by Django 3.0.8 on 2020-07-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c31', '0002_auto_20200705_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.CharField(default='cs', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
