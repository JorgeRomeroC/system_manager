from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.db.models import Max

from django.db import transaction
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    Manager personalizado para el modelo User donde el campo de login es el email.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Crea y guarda un Usuario con el email y la contraseña proporcionados.
        """
        if not email:
            raise ValueError('El usuario debe tener un email')

        extra_fields.setdefault('first_name', extra_fields.pop('nombre', ''))
        extra_fields.setdefault('last_name', extra_fields.pop('apellido', ''))

        email = self.normalize_email(email)

        # Generar el username a partir de la parte del email antes del @
        if not extra_fields.get('username'):
            username_base = email.split('@')[0]
            extra_fields['username'] = self._generate_unique_username(username_base)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Cifrar la contraseña
        user.is_staff = extra_fields.get('is_staff', False)  # Define is_staff si se pasa en extra_fields
        user.save(using=self._db)
        return user

    @transaction.atomic
    def _generate_unique_username(self, username_base):
        """
        Genera un username único basado en la parte del email antes del @.
        Si ya existe, agrega un número al final para garantizar que sea único.
        """
        # Busca los usernames que comiencen con username_base
        similar_usernames = User.objects.filter(username__startswith=username_base)

        if not similar_usernames.exists():
            return username_base

        # Filtra los usernames que siguen el patrón username_base + número
        max_suffix = \
            similar_usernames.filter(username__regex=r'^' + username_base + r'\d+$').aggregate(Max('username'))[
                'username__max']

        if max_suffix:
            suffix_number = int(max_suffix[len(username_base):]) + 1
            return f"{username_base}{suffix_number}"
        else:
            return f"{username_base}1"

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crea y guarda un superusuario con el email y la contraseña proporcionados.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='usuarios/fotos/', null=True, blank=True)
    # Fecha en la cual el usuario se esta creando
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    # La ulltima vez que el usuario hizo sesion en la plataforma
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)  # Utiliza el campo `is_active` de Django

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # Si el email de usuario se actualiza, se actualiza el username
    def save(self, *args, **kwargs):
        # Generar o regenerar el username si está vacío o si el email ha cambiado
        if not self.username or self.pk is not None:  # El usuario ya existe
            old_user = User.objects.filter(pk=self.pk).first()
            if old_user and old_user.email != self.email:
                self.username = self.email.split('@')[0]
            elif not self.username:  # Nuevo usuario o username no definido
                self.username = self.email.split('@')[0]

        # Asegurarse de que el username no sea None antes de guardar
        if not self.username:
            self.username = self.email.split('@')[0]

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'
