from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(label='E-posta')  # Adding email field manually

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Include email in fields

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class': 'form-control'})
            fields.help_text = ""
