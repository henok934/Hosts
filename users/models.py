# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.email} - {self.fname} - {self.lname} - {self.gender} - {self.phone}"


class Fedback(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=50, null=True, blank=True)

    # Adding unique related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='fedback_set',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='fedback_permissions_set',  # Unique related name
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone} {self.message}"


class Bus(models.Model):
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    sideno = models.CharField(max_length=50, null=True, blank=True)
    no_seats = models.CharField(max_length=50, null=True, blank=False)

    # Adding unique related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='bus_set',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='bus_permissions_set',  # Unique related name
        blank=True
    )

    def __str__(self):
        return f"{self.plate_no} - {self.sideno} - {self.no_seats}"    

class City(models.Model):
    depcity = models.CharField(max_length=50, null=True, blank=True)
    # Adding unique related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='city_set',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='city_permissions_set',  # Unique related name
        blank=True
    )
    def __str__(self):
        return f"{self.depcity}"

class Route(models.Model):
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    kilometer = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=50, null=True, blank=True)
    groups = models.ManyToManyField(
    'auth.Group',
    related_name='route_set',  # Unique related name
    blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='route_permissions_set',  # Unique related name
        blank=True
    )
    def __str__(self):
        return f"{self.depcity} - {self.descity}, {self.plate_no} - {self.side_no} - {self.kilometer} - {self.price} - {self.date}"





class Worker(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)  # Store hashed password
    side_no = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='worker_set',
        blank=True
    )
    worker_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='worker_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.fname} - {self.lname} - {self.gender} - {self.plate_no} - {self.side_no} - {self.phone}"



class Admin(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)  # Store hashed password
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_set',
        blank=True
    )
    admin_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_permissions_set',
        blank=True
    )
    def __str__(self):
        return f"{self.username} - {self.fname} - {self.lname} - {self.gender} - {self.password} - {self.phone}"



class Ticket(models.Model):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    no_seat = models.CharField(max_length=20, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=20, null=True, blank=True)
    plate_no = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='ticket_set',  # Unique related name
        blank=True
    )
    worker_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='ticket_permissions_set',  # Unique related name
        blank=True
    )
    def __str__(self):
        return f"{self.firstname} - {self.phone}, {self.lastname} - {self.price}, {self.descity} - {self.depcity} {self.no_seat} - {self.plate_no} - {self.side_no} - {self.date}"




"""
class Admin(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_set',
        blank=True
    )
    admin_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_permissions_set',
        blank=True
    )
    def __str__(self):
        return f"{self.fname} - {self.phone} - {self.lname} - {self.gender} - {self.email} - {self.username} - {self.password}"
"""



"""
from django.db import models

class Admin(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)  # Store hashed password

    groups = models.ManyToManyField('auth.Group', related_name='admin_set', blank=True)
    admin_permissions = models.ManyToManyField('auth.Permission', related_name='admin_permissions_set', blank=True)

    def __str__(self):
        return f"{self.fname} - {self.phone} - {self.lname} - {self.gender} - {self.email} - {self.username}"
"""






"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class Admin(AbstractUser):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    # Remove username and password as they are inherited from AbstractUser
    # username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    # password = models.CharField(max_length=128)  # Not needed

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_set',
        blank=True
    )
    admin_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.fname} - {self.phone} - {self.lname} - {self.gender} - {self.email} - {self.username}"
"""




"""
from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)  # Store hashed password

    groups = models.ManyToManyField('auth.Group', related_name='admin_set', blank=True)
    admin_permissions = models.ManyToManyField('auth.Permission', related_name='admin_permissions_set', blank=True)

    def __str__(self):
        return f"{self.fname} - {self.phone} - {self.lname} - {self.gender} - {self.email} - {self.username} - {self.password}"
"""


class Buschange(models.Model):
    new_side_no = models.CharField(max_length=50, null=True, blank=True)
    new_plate_no = models.CharField(max_length=50, null=True, blank=True)
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=20, null=True, blank=True)
    plate_no = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='buschange_set',
        blank=True
    )
    buschange_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='buschange_permissions_set',
        blank=True
    )
    def __str__(self):
        return f"{self.depcity} - {self.descity}, {self.new_side_no} - {self.new_plate_no}, - {self.plate_no} - {self.side_no} - {self.date}"

