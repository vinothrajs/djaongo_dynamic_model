from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    # eid = forms.CharField(max_length=2, required=True)
    # ename = forms.CharField(max_length=2, required=True)
    # eemail = forms.EmailField(required=True)
    # econtact = forms.CharField(max_length=2, required=True)  
    def __init__(self, field_config=None, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        
        if field_config:
            for field_data in field_config:
                field_name = field_data.get('name')
                field_type = field_data.get('type')
                max_length = field_data.get('max_length')
                required = field_data.get('required', False)
                
                if field_type == 'char':
                    self.fields[field_name] = forms.CharField(max_length=max_length, required=required)
                elif field_type == 'email':
                    self.fields[field_name] = forms.EmailField(required=required)
    class Meta:
        model = Employee
        fields = ['ename', 'eemail', 'eid', 'econtact']

# field_validations = {
#     'eid': {'required': True, 'max_length': 2},
#     'ename': {'required': True, 'max_length': 2},
#     'eemail': {'required': True},
#     'econtact': {'required': True, 'max_length': 2}
# }

# form = EmployeeForm(field_validations=field_validations)