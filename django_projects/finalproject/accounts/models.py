from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


 
 
class MyAccountManager(BaseUserManager):
 
    def create_user(self,email,username,phone,name,password=None):

        if not email:
            raise ValueError()
        if not username:
            raise ValueError()
        user  = self.model(
            email = self.normalize_email(email),
            username = username,
            name = name,
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password, phone=None,name=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            phone=phone,
            name=name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
  
class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name="email",max_length=255,unique=True)
    #required as it is for custom user imp****
    username        = models.CharField(max_length=30,unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    #*******required as it is for custom user imp
    phone           = models.CharField(max_length=10, default='', editable=False,)
    name            = models.CharField(max_length=50, default='', editable=False,)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone', 'name']
    objects = MyAccountManager()
 
    def __str__(self):
        return self.email
   
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)
    phonenumber=models.TextField()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class cities(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class mysub(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE) #userid
	name=models.CharField(max_length=100)
	city=models.ForeignKey(cities,on_delete=models.CASCADE)
	district=models.TextField()
	pg_type=models.TextField()
	time=models.TextField()
	status=models.TextField()
	
	def __str__(self,arg):
		return self.name		

class contact_info(models.Model):
	contact_name=models.CharField(max_length=100)
	contact_email=models.EmailField()
	contact_message=models.TextField()

	def __str__(self):
		return self.contact_name	

class Images(models.Model):
	mysub = models.ForeignKey(mysub,on_delete=models.CASCADE)
	image = models.FileField(upload_to = 'media/uploads',null=True)
	
	def __str__(self):
 		return self.image

class Notification(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	mysub = models.ForeignKey(mysub,on_delete=models.CASCADE)
	message_not=models.TextField()

	def __str__(self):
 		return self.message_not


		