from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        # widgets = {
        #     'first_name': TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'})
        # }

    # def __init__(self, *args, **kwargs):
    #     super(NewAccountForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #
    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email')
        username_value = field_data.get('username')
        if User.objects.filter(email=email_value).exists():
            self._errors['email'] = self.error_class(["This email address is already being used."])
        if User.objects.filter(username=username_value).exists():
            self._errors['username'] = self.error_class(['This username is already being used.'])
        return field_data