from django.db import models
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django import forms


class ContactFormModel(models.Model):
    name = models.CharField(blank=True,max_length=20)
    message = models.CharField(blank=True,max_length=20)
    emaill = models.CharField(blank=True,max_length=20)
    subject = models.CharField(blank=True,max_length=20)
    user = models.OneToOneField(User,null=True,on_delete=models.SET_NULL)
    password = models.CharField(max_length=20,blank=True)
    

    def __str__(self):
        return self.name



class CForm(ModelForm):
    class Meta:
        model = ContactFormModel
        fields=['name','password']
        widgets = {'password':forms.PasswordInput}

        def get_user_model(self):
            return self.user.username

        def get_absolute_url(self):
            return reverse('login',kwargs={'pk':self.pk})


class Pixxx(models.Model):
     
    title = models.CharField(blank=True,max_length=20)
    slug = models.SlugField()
    image = models.ImageField(blank=True,upload_to='img/')


    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src = "{}" width="200" height="200"/>'.format (self.image.url))
    image_tag.short_description = 'Image'



# Create your models here.
