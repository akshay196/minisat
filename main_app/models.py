from django.db import models
# import the models class

# Create your models here.
# Create a class that inherits from models.Model so that Django knows we're creating a model.


# Model for Compute_resources
class Compute_resource_model(models.Model):
    name = models.CharField(max_length=10, unique=True)
    ip_address = models.CharField(max_length=15, unique=True)
    root_password = models.CharField(max_length=20)

    # Use special model types that correspond to databases types.

    def __str__(self):
        # Use self.name to display in databases.
        return self.name


# Model for profile
class Profile_model(models.Model):
    profile_name = models.CharField(max_length=10)
    ram = models.IntegerField()
    cpus = models.IntegerField()
    disk_size = models.IntegerField()

    def __str__(self):
        return self.profile_name


# Model for operating_system
class Operating_system_model(models.Model):
    os_name = models.CharField(max_length=15)
    os_location = models.CharField(max_length=100)

    def __str__(self):
        return self.os_name


# Model for create host
class Create_host_model(models.Model):
    vm_name = models.CharField(max_length=15)
    vm_os = models.CharField(max_length=15)
    select_vm_profile = models.CharField(max_length=10)
    select_compute = models.CharField(max_length=10)

    def __str__(self):
        return self.vm_name


# Model for new container
class Container_model(models.Model):
    select_compute = models.CharField(max_length=20)
    image_name = models.CharField("Image Name", max_length=20)
    tag_name = models.CharField("Tag", max_length=20)
    container_name = models.CharField("Container Name", max_length=20)

    def __str__(self):
        return self.container_name
