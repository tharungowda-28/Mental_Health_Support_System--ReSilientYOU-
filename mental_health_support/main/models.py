from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)


class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True, null=True)
    content = models.TextField()
    external_url = models.URLField()
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)  # Add this line

    def __str__(self):
        return self.title

class Journal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    image = models.ImageField(upload_to='journal_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    # Other fields...

class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True, null=True)
    url = models.URLField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Image field

    def __str__(self):
        return self.title
    # Other fields...

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    # Other fields...

class YogaAsana(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='yoga_asanas/')
    description = models.TextField()

    def __str__(self):
        return self.name

class YogaDetail(models.Model):
    asana = models.OneToOneField(YogaAsana, on_delete=models.CASCADE)
    steps = models.TextField()
    benefits = models.TextField()
    video_url = models.URLField(max_length=200, blank=True) 

    def __str__(self):
        return self.asana.name


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='quiz_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey('Quiz', related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.text

class Therapist(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='therapists/')
    specialization = models.CharField(max_length=255)
    available_slots = models.CharField(max_length=255, blank=True, null=True)  # e.g., "Mon-Fri: 9 AM - 5 PM"
    experience = models.PositiveIntegerField(default=0)  # Years of experience
    location = models.CharField(max_length=255, blank=True, null=True)
    languages = models.CharField(max_length=150, blank=True, null=True)
    about = models.CharField(max_length= 1000)

    def __str__(self):
        return self.name

class Consultation(models.Model):
    therapist = models.ForeignKey('Therapist', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.therapist.name} on {self.date} at {self.time}'

