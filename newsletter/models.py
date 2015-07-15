from django.db import models

# Create your models here.c

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(blank=False, null=True, max_length=150)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

#https://docs.djangoproject.com/en/1.8/ref/forms/fields/

	def __str__(self):
		return str(self.email)