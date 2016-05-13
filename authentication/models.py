from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class EmployeeManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        employee = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        employee.set_password(password)
        employee.save()

        return employee

    def create_superuser(self, email, password, **kwargs):
        employee = self.create_user(email, password, **kwargs)

        employee.is_admin = True
        employee.save()

        return employee


class Employee(AbstractBaseUser):
    # Choices
    EMPLOYEE_ROLE = (
        ("C", "CEO"),
        ("M", "Manager"),
        ("P", "Project Lead"),
        ("S", "Software Developer"),
        ("J", "Junior Software Developer"),
        ("H", "HR Manager"),
        ("Q", "Quality Assurance Engineer"),
    )
    # Fields
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    # role = models.CharField(max_length=1, choices=EMPLOYEE_ROLE)
    role = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name