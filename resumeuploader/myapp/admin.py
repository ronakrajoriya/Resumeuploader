from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
  list_display=['id','name','dob','gender','state','locality','city','pin','email','job_city','profile_image','my_file']

