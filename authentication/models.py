from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class EmployeeManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        employee = self.model(
            email=self.normalize_email(email), username=kwargs.get('username'), role=kwargs.get('role')
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
        ("CEO", "CEO"),
        ("Manager", "Manager"),
        ("Project Lead", "Project Lead"),
        ("Software Developer", "Software Developer"),
        ("Junior Software Developer", "Junior Software Developer"),
        ("HR Manager", "HR Manager"),
        ("Quality Assurance Engineer", "Quality Assurance Engineer"),
    )
    # Fields
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    role = models.CharField(max_length=100, choices=EMPLOYEE_ROLE)
    #role = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EmployeeManager()

    #USERNAME_FIELD = 'email' REQUIRED_FIELDS = ['username', 'role']
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']                # required fields are only for user model .... should include all blank = False fields

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name






