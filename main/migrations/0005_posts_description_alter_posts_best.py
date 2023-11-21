# Generated by Django 4.2.7 on 2023-11-21 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_posts_best'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات کوتاه'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='best',
            field=models.BooleanField(default=False, verbose_name=' بهترین مقالات'),
        ),
    ]