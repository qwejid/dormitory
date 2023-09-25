from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator, MaxValueValidator,MinLengthValidator,MaxLengthValidator


def user_directory_path(instance, filename):
    # Генерируем путь к медиафайлу на основе имени пользователя
    return 'users/{0}/{1}'.format(instance.user.username, filename)

contract_number_validator = RegexValidator(
    regex=r'^\d{6}/\d{3}$',  # Проверяем, что строка имеет вид "Шесть цифр/Три цифры"
    message="Формат номера договора должен быть 042020/232"
)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    room = models.IntegerField(
        validators=[MaxValueValidator(9999)],  # Максимальное значение 9999 (4 цифры)
        help_text="Введите номер комнаты",null=True
    )
    contract_number = models.CharField(
        max_length=10,  # Максимум 10 символов (9 цифр + слэш)
        validators=[contract_number_validator],
        help_text="Формат: 750256/380",null=True
    )
    student_ID = models.CharField(
        max_length=6,  # Максимум 6 символов
        validators=[
            MinLengthValidator(limit_value=6, message="Должно быть ровно 6 символов"),
            MaxLengthValidator(limit_value=6, message="Должно быть ровно 6 символов")
        ],  
        help_text="Ровно 6 символов",null=True
    )
    class Meta:
        verbose_name_plural = "Профили"


    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
    

    def save(self, *args, **kwargs):
        # Проверяем, была ли фотография изменена
        if self.pk:  # Если объект уже существует
            try:
                old_instance = Profile.objects.get(pk=self.pk)
                if old_instance.photo and self.photo != old_instance.photo:
                    # Удаляем старый файл фотографии из медиа
                    if os.path.isfile(old_instance.photo.path):
                        os.remove(old_instance.photo.path)
            except Profile.DoesNotExist:
                pass

        super(Profile, self).save(*args, **kwargs)
    
    

