from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    address = forms.CharField(label = "address")

    class Meta:
        model = User
        fields = ("username", "address", "email", )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        address = self.cleaned_data["address"]
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user