from django import forms
from django.contrib.auth.models import User
from django.core import validators
from first_app.models import Webpage, Topic, AccessRecord, UserProfileInfo


class NewTopic(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


class NewWebpage(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'


class NewAccessrecord(forms.ModelForm):
    class Meta:
        model = AccessRecord
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio', 'picture')
