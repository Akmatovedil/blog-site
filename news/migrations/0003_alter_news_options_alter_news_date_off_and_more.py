# Generated by Django 4.2 on 2023-04-24 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_date_off_news_likes_news_rating_news_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='date_off',
            field=models.DateField(null=True, verbose_name='Дата окончания новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.URLField(verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='news',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.news')),
            ],
        ),
    ]
