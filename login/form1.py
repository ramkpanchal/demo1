import re
from django import forms 
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as

class RegistrationForm(forms.Form):
username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=true, max_length = 30)), lable= _("username"), error_messages ={'invalid'("please enter username.")} )
Email= forms.EmailField(widget=forms.TextInput(attrs=dict(required=true, max_length = 30)), lable= _("EmailId") )
password1= forms.CharField(widget=forms.TextInput(attrs=dict(required=true, max_length = 30, render_value = False)), lable= _("password1") )
password2= forms.CharField(widget=forms.TextInput(attrs=dict(required=true, max_length = 30, render_value = False)), lable= _("password2") )


def clean_username(self):
	try:
		user = user.objects.get(username_iexact= self.cleaned_data['username'])
	except User.DoesNotExist:
		return self.cleaned_data['username']
		raise forms.ValidationsError(_("The username already exists/ please try another one"))

def clean(self): 
	if 'password' in self.clean_data and 'password' in self.cleaned_data:
		if self.clean_data['password'] != self.cleaned_data['password2':
		raise forms.ValidationError(_("the two password fields did not match"))]
		return self.cleaned_data
