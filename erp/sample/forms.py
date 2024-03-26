from django import forms
from .models import Contact  
from .employee.models import Employee 

from django.utils.translation import gettext_lazy as _

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'email', 'phone_number']
        
class ContactForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'))
    email = forms.EmailField(label=_('Email'))
    phone_number = forms.CharField(label=_('Phone Number'),)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number']