# Generated by Django 3.0.3 on 2020-04-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0007_auto_20200405_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]
