from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(max_length = 150)
	email = forms.EmailField()
	subject = forms.CharField()
	message = forms.CharField()

	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	email_base, provider = email.split("@")
	# 	domain, extension = provider.split('.')
	# 	if not domain == "user":
	# 		raise forms.ValidationError("Please use your user email address")
	# 	if not extension == "edu":
	# 		raise forms.ValidationError("Please use a user.edu email address")

	# 	return email
 

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
		#exlcude is an option

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain == "user":
			raise forms.ValidationError("Please use your user email address")
		if not extension == "edu":
			raise forms.ValidationError("Please use a user.edu email address")

		return email
#many more forms.**** https://docs.djangoproject.com/en/1.8/ref/forms/fields/#built-in-fields

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#could write validation code here
		return full_name