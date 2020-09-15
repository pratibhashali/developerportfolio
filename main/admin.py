from django.contrib import admin

# Register your models here.
from main.models import AboutMe, Education, EducationResponsibilities , Experience , ExperienceResponsibilities, Publication , Skill, Achievement

admin.site.register(AboutMe)
admin.site.register(Education)
admin.site.register(EducationResponsibilities)
admin.site.register(Experience)
admin.site.register(ExperienceResponsibilities)
admin.site.register(Publication)
admin.site.register(Skill)
admin.site.register(Achievement)
