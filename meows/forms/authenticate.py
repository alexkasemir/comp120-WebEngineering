from django import forms

class AuthenticationForm(forms.Form):
	username = forms.CharField(widget=forms.widgets.TextInput)
	password = forms.CharField(widget=forms.widgets.PasswordInput)

	class Meta:
		fields = ['usrname', 'password']


