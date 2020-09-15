from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactForm, AboutMe, Education, EducationResponsibilities , Experience , ExperienceResponsibilities, Publication , Skill, Achievement
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def home(request):
    if request.method == 'POST':
        contact_us = ContactForm(request.POST)
        if contact_us.is_valid():
            name = contact_us.cleaned_data.get('name')
            email = contact_us.cleaned_data.get('email')
            message = contact_us.cleaned_data.get('message')
            # send email code goes here
            
            subject, from_email = f'Contact request from personal website by - {name}', email
            text_content = 'Hi I am, {name}. {message} Sender Details: Name: {name} Email: {email}'
            html_content = f'<p>Hi I am, <strong>{name} <strong>,<br/><br/><br/> {message} <br/><br/><br/><br/>Sender Details: <br/>Name: {name}<br/>Email: {email}</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [settings.EMAIL_RECEIVER])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(
                request, f'Thanks for contacting us! We will get back to you soon.')
            
            return redirect('main-home')
    else:
        contact_us = ContactForm()

    about_me = AboutMe.objects.first()
    educations = Education.objects.all().order_by('-start_date')
    educationResponsibilities = EducationResponsibilities.objects.all()
    experienceResponsibilities = ExperienceResponsibilities.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    publications = Publication.objects.all()
    skills = Skill.objects.all()
    achievements = Achievement.objects.all().order_by('-year')
    
    data = {
        'about_me' : about_me,
        'educations' : educations,
        'educationResponsibilities':educationResponsibilities,
        'experienceResponsibilities' : experienceResponsibilities,
        'experiences' : experiences,
        'publications' : publications,
        'skills' : skills,
        'achievements' : achievements,
        'contact_us':contact_us
    }
    
    return render(request, 'main/index.html', data)
