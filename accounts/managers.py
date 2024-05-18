from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, username, mobile, password=None, **other_fields):
        if username is None:
            raise ValueError('Username is required !')
        elif mobile is None:
            raise ValueError('Mobile number is required')
        user = self.model(
            username=username,
            mobile=mobile,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, mobile, password=None, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        if other_fields.get('is_active') is not True:
            raise ValueError('For superuser is_active is required !')
        if other_fields.get('is_staff') is not True:
            raise ValueError('For superuser is_staff is required !')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('For superuser is_superuser is required !')
        return self.create_user(username, mobile, password, **other_fields)
