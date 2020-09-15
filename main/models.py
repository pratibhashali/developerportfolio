from django.db import models
from django import forms


class Education(models.Model):
    college_name = models.CharField(max_length = 200)
    start_date = models.DateField()
    end_date = models.DateField()
    degree = models.CharField(max_length = 100)
    stream = models.CharField(max_length = 100)

    def __str__(self):
        return self.college_name

class EducationResponsibilities(models.Model):
    description = models.CharField(max_length = 1000)
    education = models.ForeignKey(Education, on_delete=models.CASCADE,)
    def __str__(self):
        return self.description[:20] + ", " + self.education.college_name


class Experience(models.Model):
    company_name = models.CharField(max_length = 150)
    profile = models.CharField(max_length = 150)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.company_name


class ExperienceResponsibilities(models.Model):
    description = models.CharField(max_length = 1000)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE,)
    def __str__(self):
        return self.description[:20] + ", " + self.experience.company_name

class Publication(models.Model):
    paper_title = models.CharField(max_length = 150)
    paper_abstract = models.TextField()
    paper_published_date = models.DateField()
    def __str__(self):
        return self.paper_title

class AboutMe(models.Model):
    about_me = models.TextField()
    name = models.CharField(max_length = 100)
    my_summary = models.CharField(max_length=200) # Research Scholar | Food Scientist | Workaholic | Nutritionist | Social Activist
    resume = models.FileField(upload_to = 'resume/')
    def __str__(self):
        return self.name
        
class Skill(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Achievement(models.Model):
    description = models.CharField(max_length = 500)
    year = models.CharField(max_length=200, null = True)
    order_in = models.IntegerField(unique=True)
    def __str__(self):
        return f"Order: {self.order_in}" + " " +self.year + " " + self.description

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))
