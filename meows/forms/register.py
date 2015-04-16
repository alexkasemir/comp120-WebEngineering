from django import forms
from meows.models import User

class RegistrationForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ['username', 'email', 'password', 'conf_password']
                # widgets = {
                #     'password': forms.PasswordInput(),
                # }

        username = forms.CharField(widget=forms.TextInput,label="username")
        #username = forms.CharField(label="username")
        email = forms.EmailField(widget=forms.TextInput,label="Email")
        #email = forms.EmailField(label="Email")
    	password = forms.CharField(widget=forms.PasswordInput, label="Password")
        #password = forms.CharField(label="Password")
    	conf_password = forms.CharField(widget=forms.PasswordInput, label="Password (again)")
        #conf_password = forms.CharField(label="Password (again)")

    	def clean(self):
    		cleaned_data = super(RegistrationForm, self).clean()
    		if 'password' in self.cleaned_data and 'conf_password' in self.cleaned_data:
                        if self.cleaned_data['password'] != self.cleaned_data['conf_password']:
    		          raise forms.ValidationError("Passwords do not seem to match. Try again")
    		return self.cleaned_data
        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
