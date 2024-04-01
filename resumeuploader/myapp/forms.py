from django import forms
from .models import Resume


GENDER_CHOICE=[
  ('Male','Male'),
  ('Female','Female')
]
JOB_CITY_CHOICE=[
  ('Delhi','Delhi'),
  ('Pune','Pune'),
  ('Mumbai','Mumbai'),
  ('Indore','Indore'),
  ('Banglore','Banglore')
]

class ResumeForm(forms.ModelForm):
  gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect) 
  job_city= forms.MultipleChoiceField(label='Prefered Job Locations', choices=JOB_CITY_CHOICE, widget= forms.CheckboxSelectMultiple)
  class Meta:
    model = Resume
    fields = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
    labels = {'name':'Full Name','dob': 'Date of Birth','pin':'Pin Code','mobile':'Mobile No.','profile_image':'Profile Image','my_file':'Document','email':'Email ID'}
    widgets={
      'name':forms.TextInput(attrs={'class':'form-control'}),
      'dob':forms.DateInput(attrs={'class':'form-control'}),
      'locality':forms.TextInput(attrs={'class':'form-control'}),
      'city':forms.TextInput(attrs={'class':'form-control'}),
      'state':forms.TextInput(attrs={'class':'form-control'}),
      'pin':forms.NumberInput(attrs={'class':'form-control'}),
      'mobile':forms.NumberInput(attrs={'class':'form-control'}),
      'email':forms.EmailInput(attrs={'class':'form-control'}),
    }