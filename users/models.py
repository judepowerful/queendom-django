from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


def upload_location(instance, filename, **kwargs):
    file_path = 'profile/{user_account_email}/{filename}'.format(
        user_account_fullname = str(instance.user.email), 
        filename=filename,
        )
    return file_path

class MyAccountManager(BaseUserManager):
	def create_user(self, email, netid, full_name, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not full_name:
			raise ValueError('Users must have a full name')

		user = self.model(
			email=self.normalize_email(email),
			netid=self.normalize_email(email).split('@')[0],
			full_name=full_name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, full_name, password):
		user = self.create_user(
			email=self.normalize_email(email),
			netid=self.normalize_email(email).split('@')[0],
			password=password,
			full_name=full_name,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	netid					= models.CharField(max_length=30, unique=True)
	full_name				= models.CharField(max_length=60, unique=False)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['full_name']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
	bio = models.TextField(blank=True)
	profileimg = models.ImageField(upload_to=upload_location, default='default_profile_img.jpg')
	location = models.CharField(max_length=100, blank=True)

	def get_email(self):
		return self.user.email

	def __str__(self):
		return self.user.email

