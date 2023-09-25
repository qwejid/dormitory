# Generated by Django 4.2.5 on 2023-09-24 10:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0009_news_author_alter_product_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                ("photo", models.ImageField(blank=True, upload_to="users/%Y/%m/%d")),
                (
                    "room",
                    models.IntegerField(
                        help_text="Введите номер комнаты",
                        validators=[django.core.validators.MaxValueValidator(9999)],
                    ),
                ),
                (
                    "contract_number",
                    models.CharField(
                        help_text="Формат: 750256/380",
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Формат номера договора должен быть 042020/232",
                                regex="^\\d{6}/\\d{3}$",
                            )
                        ],
                    ),
                ),
                (
                    "student_ID",
                    models.CharField(
                        help_text="Ровно 6 символов",
                        max_length=6,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                limit_value=6, message="Должно быть ровно 6 символов"
                            ),
                            django.core.validators.MaxLengthValidator(
                                limit_value=6, message="Должно быть ровно 6 символов"
                            ),
                        ],
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]