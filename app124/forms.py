from django import forms
from .models import UserModel

GENDER_CHOICES=[('Male','Male'),('FeMale','FeMale'),('Others','Others')]

class UserForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,
                             widget=forms.RadioSelect)
    class Meta:
        model=UserModel
        fields=['name','dob','contact_no','gender','pin','city','state',
                    'gmail','password','profile_image']
        labels={'name':'Full Name','gmail':'Email Id','profile_image':'Image'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'contact_no':forms.NumberInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'gmail':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True)
        }
class UserloginForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=['gmail','password']

        labels={'gmail':'Mail_id'}
        widgets={'gmail':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True)}