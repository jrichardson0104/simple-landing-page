from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__", "timestamp", "updated"]
	#class Meta:
		#model = SignUp
	form = SignUpForm


admin.site.register(SignUp, SignUpAdmin)


#admin options at https://docs.djangoproject.com/en/1.8/ref/contrib/admin/