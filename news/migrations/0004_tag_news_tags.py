# Generated by Django 4.2 on 2023-04-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_options_alter_news_date_off_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, to='news.tag'),
        ),
    ]
