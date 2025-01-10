from django import forms
from .models import UserModel  # Import the UserModel correctly

class usersForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        }
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email = forms.EmailField(required=True, label="Your Email")
    phone = forms.CharField(required=True, label="Your Phone")
    website = forms.CharField(required=True, label="Your Website")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Your Message")