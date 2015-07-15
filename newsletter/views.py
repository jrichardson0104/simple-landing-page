from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.template import Template, Context, loader 
# Create your views here.
def home(request):
	title = 'Welcome'
	# if request.user.is_authenticated():
	# 	title = "Welcome %s" %(request.user)
	#can add a form here



	# if request.method == "POST":
	# 	print (request.POST) 

	form = SignUpForm(request.POST or None)# without none it runs through validaters
	#if no post data then don't run
	message = "Sign Up Below"
	context = {
		"title": title,
		"form": form,
		"message": message,
	}
	if form.is_valid():
		#form.save() 
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "Unknown User"
		instance.save()
		context = {
			"message": "Thank You %s!" %(instance.full_name) 

		}
		#print (instance.email, instance.full_name)


	return render(request, "home.html", context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#print (form.cleaned_data)
		form_email = form.cleaned_data.get('email')
		form_full_name = form.cleaned_data.get('full_name')
		form_message = form.cleaned_data.get('message')
		form_subject = form.cleaned_data.get('subject')
		#print (form_message,form_email,form_full_name)
		#if you had allot of fields you could 
		#for key, value in form.cleaned_data.iteritems():
			#print (key, value)
		#subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_email, 'otheremailaddress', 'and so on']
		contact_message = "%s: %s via %s"%(form_full_name,
											form_message, 
											form_email)
		some_html_message = """ <h1>Hello</h1> """

		send_mail(form_subject,
				contact_message,
				from_email,
				to_email,
				html_message = some_html_message,
				fail_silently=True) #will run server error if false
	context = {
		"form": form,

	}

	return render(request, "forms.html", context)


# def register(request):
# 	form = ContactForm(request.POST or None)
# 	if form.is_valid():
# 		#print (form.cleaned_data)
# 		form_email = form.cleaned_data.get('email')
# 		form_full_name = form.cleaned_data.get('full_name')
# 		form_message = form.cleaned_data.get('message')
# 		form_subject = form.cleaned_data.get('subject')
# 		#print (form_message,form_email,form_full_name)
# 		#if you had allot of fields you could 
# 		#for key, value in form.cleaned_data.iteritems():
# 			#print (key, value)
# 		#subject = 'Site Contact Form'
# 		from_email = settings.EMAIL_HOST_USER
# 		to_email = [form_email, 'otheremailaddress', 'and so on']
# 		contact_message = "%s: %s via %s"%(form_full_name,
# 											form_message, 
# 											form_email)
# 		some_html_message = """ <h1>Hello</h1> """

# 		send_mail(form_subject,
# 				contact_message,
# 				from_email,
# 				to_email,
# 				html_message = some_html_message,
# 				fail_silently=True) #will run server error if false
# 	context = {
# 		"form": form,

# 	}

# 	return render(request, "forms.html", context)
