# Generated by Django 4.2.5 on 2023-09-29 12:24

import account.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_alter_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="contract_number",
            field=models.CharField(
                help_text="Формат: 750256/380",
                max_length=10,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Формат номера договора должен быть 042020/232",
                        regex="^\\d{6}/\\d{3}$",
                    )
                ],
                verbose_name="Номер договора",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=account.models.user_directory_path,
                verbose_name="Фото",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="room",
            field=models.IntegerField(
                help_text="Введите номер комнаты",
                null=True,
                validators=[django.core.validators.MaxValueValidator(9999)],
                verbose_name="Номер комнаты",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="student_ID",
            field=models.CharField(
                help_text="Ровно 6 символов",
                max_length=6,
                null=True,
                validators=[
                    django.core.validators.MinLengthValidator(
                        limit_value=6, message="Должно быть ровно 6 символов"
                    ),
                    django.core.validators.MaxLengthValidator(
                        limit_value=6, message="Должно быть ровно 6 символов"
                    ),
                ],
                verbose_name="Номер студенческого",
            ),
        ),
    ]
