# Generated by Django 2.0.7 on 2018-08-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sberbank', '0002_auto_20180802_1820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logentry',
            options={'ordering': ['-created'], 'verbose_name': 'запись в журнале', 'verbose_name_plural': 'записи в журнале'},
        ),
        migrations.RemoveField(
            model_name='logentry',
            name='request_type',
        ),
        migrations.AddField(
            model_name='logentry',
            name='action',
            field=models.CharField(db_index=True, default='old', max_length=100, verbose_name='action'),
            preserve_default=False,
        ),
    ]