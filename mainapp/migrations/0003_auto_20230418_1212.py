# Generated by Django 3.1.14 on 2023-04-18 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20230418_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField()),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('level', models.PositiveIntegerField(default=1, verbose_name='Уровень')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='mainapp.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='mainapp.menuitem')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
        migrations.DeleteModel(
            name='TreeMenu',
        ),
    ]