from django.contrib.auth.base_user import BaseUserManager


class NewUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        """
        Функция для внутреннего пользователя.
        Создаёт и сохраняет пользователя с переданным email и паролем в базу данных
        """

        if not email:
            raise ValueError('Почта должна быть установлена')
        if not password:
            raise ValueError('Пароль должен быть установлен')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, username=None, **extra_fields):
        """
        Функция обертка создания обычного пользователя, без привилегий суперпользователя или персонала (к примеру админ)
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, password, username=None, **extra_fields):
        """
        Функция обертка создания пользователя с привилегиями суперпользователя
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, username, password, **extra_fields)
