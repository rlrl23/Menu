# Generated by Django 3.1.14 on 2023-04-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treemenu',
            old_name='name',
            new_name='title_name',
        ),
        migrations.AddField(
            model_name='treemenu',
            name='menu_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]