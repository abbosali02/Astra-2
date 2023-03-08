import imghdr
from django.shortcuts import reverse
from django.db import models

# Create your models here.
class contactMe(models.Model):
    
    name = models.CharField('Name', max_length=300)
    last = models.CharField('Last', max_length=300)
    age = models.CharField('Age', max_length=100)
    phone = models.CharField('Phone', max_length=100)
    email = models.EmailField('Email')
    telegram = models.CharField('Telegram', max_length=300)
   

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.name


class Results(models.Model):
    title = models.CharField('title', max_length=300)
    seven = models.CharField('seven', max_length=300)
    sevenhalf = models.CharField('sevenhalf', max_length=300)
    eight = models.CharField('eight', max_length=300)
    eighthalf = models.CharField('eighthalf', max_length=300)

    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Result'

    def __str__(self):
        return self.title

class Apply(models.Model):
    
    name = models.CharField('Name', max_length=300)
    age = models.CharField('Age', max_length=100)
    residence = models.CharField('Place of Residence', max_length=300)
    phone = models.CharField('Phone', max_length=100)
    education = models.CharField('Education Status', max_length=300)
    university = models.CharField('University Major', max_length=300)
    ielts = models.CharField('IELTS BAND Score', max_length=300)
    other = models.CharField('Other Achievements', max_length=300)
    job1 = models.CharField('Employer#1', max_length=300)
    job2 = models.CharField('Employer#2', max_length=300)
    languages = models.CharField('Other Languages', max_length=300)
    telegram = models.CharField('Telegram', max_length=300)
   

    class Meta:
        verbose_name = 'Apply Us'
        verbose_name_plural = 'Apply Us'

    def __str__(self):
        return self.name
        

class Seven(models.Model):
    slug = models.SlugField('unique number', unique=True)
    img = models.ImageField('Image', db_index=True)
    title = models.CharField('Title', max_length=10000)
    desciption = models.CharField('Description', max_length=10000)
    subtitle = models.CharField('Subtitle', max_length=10000)
   
    text = models.TextField('Text', max_length=10000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=10000)
    

    class Meta:
        verbose_name = 'Seven'
        verbose_name_plural = 'Seven'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('seven_detail_url', kwargs={'slug': self.slug})

class SevenHalf(models.Model):
    slug = models.SlugField('unique number', unique=True)
    img = models.ImageField('Image', db_index=True)
    title = models.CharField('Title', max_length=10000)
    desciption = models.CharField('Description', max_length=10000)
    subtitle = models.CharField('Subtitle', max_length=10000)
   
    text = models.TextField('Text', max_length=10000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=10000)
    

    class Meta:
        verbose_name = 'SevenHalf'
        verbose_name_plural = 'SevenHalf'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sevenhalf_detail_url', kwargs={'slug': self.slug})

class Eight(models.Model):
    slug = models.SlugField('unique number', unique=True)
    img = models.ImageField('Image', db_index=True)
    title = models.CharField('Title', max_length=10000)
    desciption = models.CharField('Description', max_length=10000)
    subtitle = models.CharField('Subtitle', max_length=10000)
   
    text = models.TextField('Text', max_length=10000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=10000)
    

    class Meta:
        verbose_name = 'eight'
        verbose_name_plural = 'eight'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('eight_detail_url', kwargs={'slug': self.slug})

class EightHalf(models.Model):
    slug = models.SlugField('unique number', unique=True)
    img = models.ImageField('Image', db_index=True)
    title = models.CharField('Title', max_length=10000)
    desciption = models.CharField('Description', max_length=10000)
    subtitle = models.CharField('Subtitle', max_length=10000)
   
    text = models.TextField('Text', max_length=10000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=10000)
    

    class Meta:
        verbose_name = 'EightHalf'
        verbose_name_plural = 'EightHalf'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('eighthalf_detail_url', kwargs={'slug': self.slug})

class Team(models.Model):
    slug = models.SlugField('unique number', unique=True)
    img = models.ImageField('Image', db_index=True)
    title = models.CharField('Name', max_length=300)
    desciption = models.CharField('Description', max_length=500)
    subtitle = models.CharField('Subtitle', max_length=500)
   
    text = models.TextField('Text', max_length=5000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=1000)
    

    class Meta:
        verbose_name = 'Team Members'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('team_detail_url', kwargs={'slug': self.slug})

class FirstTeacher(models.Model):
    little = models.CharField('Position', max_length=300)
    slug = models.SlugField('unique number', unique=True)
    img = models.ImageField('Image', db_index=True)
    title = models.CharField('Name', max_length=300)
    desciption = models.CharField('Description', max_length=500)
    subtitle = models.CharField('Subtitle', max_length=500)
   
    text = models.TextField('Text', max_length=5000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=1000)
    

    class Meta:
        verbose_name = 'MukhammadAli'
        verbose_name_plural = 'MukhammadAli'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('first_detail_url', kwargs={'slug': self.slug})

class SecondTeacher(models.Model):
    little = models.CharField('Position', max_length=300)
    slug = models.SlugField('unique number', unique=True)
    img = models.ImageField('Image', db_index=True)
    title = models.CharField('Name', max_length=300)
    desciption = models.CharField('Description', max_length=500)
    subtitle = models.CharField('Subtitle', max_length=500)
   
    text = models.TextField('Text', max_length=5000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=1000)
    

    class Meta:
        verbose_name = 'Alisher'
        verbose_name_plural = 'Alisher'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('second_detail_url', kwargs={'slug': self.slug})
    

class ThirdTeacher(models.Model):
    little = models.CharField('Position', max_length=300)
    slug = models.SlugField('unique number', unique=True)
    img = models.ImageField('Image', db_index=True)
    title = models.CharField('Name', max_length=300)
    desciption = models.CharField('Description', max_length=500)
    subtitle = models.CharField('Subtitle', max_length=500)
   
    text = models.TextField('Text', max_length=5000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=1000)
    

    class Meta:
        verbose_name = 'Third team'
        verbose_name_plural = 'Third Team'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('third_detail_url', kwargs={'slug': self.slug})
    
class HeadTeacher(models.Model):
    little = models.CharField('Position', max_length=300)
    slug = models.SlugField('unique number', unique=True)
    
    title = models.CharField('Name', max_length=300)
    desciption = models.CharField('Description', max_length=500)
    subtitle = models.CharField('Subtitle', max_length=500)
   
    text = models.TextField('Text', max_length=5000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=1000)
    

    class Meta:
        verbose_name = 'Head Teacher'
        verbose_name_plural = 'Head Teacher'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('head_detail_url', kwargs={'slug': self.slug})
    
class MainTeacher(models.Model):
    little = models.CharField('Position', max_length=300)
    slug = models.SlugField('unique number', unique=True)
    
    title = models.CharField('Name', max_length=300)
    desciption = models.CharField('Description', max_length=500)
    subtitle = models.CharField('Subtitle', max_length=500)
   
    text = models.TextField('Text', max_length=5000)
    img3 = models.ImageField('Image', db_index=True)
    headtitle = models.CharField('Headtitle', max_length=1000)
    

    class Meta:
        verbose_name = 'Main Teacher'
        verbose_name_plural = 'Main Teacher'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main_detail_url', kwargs={'slug': self.slug})

