from django.db import models

from phone_field import PhoneField
from summary.models import summaryModel
from django.db.models.signals import pre_save
from event_management.utils import unique_slug_generator

class Logo(models.Model):
    logo = models.ImageField(default= 'test')

class Event(models.Model):
    STATUS_MODE = (
        ('private', 'Private'),
        ('public', 'Public')
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True) 
    starting_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    program = models.ManyToManyField('Program')
    status = models.CharField(max_length=10, choices= STATUS_MODE)
    location = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Event)

class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30,)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    attend_status_choice = (
        ('waiting', 'Waiting'),
        ('attending', 'Attending'),
        ('completed', 'Completed'),
        ('absent', 'Absent'),
        ('cancelled', 'Cancelled'),
    )
    attend_status = models.CharField(
        choices=attend_status_choice, default='Absent',  max_length=10)
   # created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventmember_created_user')
   # updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventmember_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(choices=status_choice, default = 'Active', max_length=10)


    class Meta:
        unique_together = ['event', 'phone']

    def __str__(self):
        return str(self.full_name)
    
    # def get_absolute_url(self):
    #     return reverse('join-event-list')

class Speaker(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    phone = PhoneField(blank=False)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    telegram =  models.URLField(blank=True)
    picture = models.ImageField(default=True)
    job = models.CharField(max_length=100, blank=True, default=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    topic = models.CharField(max_length=100)
    description = models.TextField()
    starting_date = models.DateTimeField()
    end_date = models.DateTimeField()
    speaker = models.ManyToManyField('Speaker')
    venue = models.ForeignKey('Venue', on_delete = models.CASCADE)

    def __str__(self):
        return self.topic

class Venue(models.Model):
    place = models.CharField(max_length=100)
    location = models.URLField()

    def __str__(self):
        return self.place
    
class Sponsor(models.Model):
    name= models.CharField(max_length=50)
    image = models.ImageField()
    level_choice = (
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('platinum', 'Platinum'),
    )
    sponsor_level = models.CharField(choices =level_choice, max_length=50)   

    def __str__(self):
        return self.name    

class Galary(models.Model):
    image = models.ImageField(default=True)

class Summary(models.Model):
    
    summary =models.ForeignKey(summaryModel, on_delete=models.CASCADE)
    day = models.DateTimeField(blank=True) 
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    image = models.ImageField()   


