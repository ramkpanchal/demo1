from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

@csrf_protect
def register(request):
	if request.method == "post":
		form = RegistrationForm(request.POST)
	if form.is_valid():
		user = user.object.create.user(
		username = form.cleaned_data['username'],
		email = form.cleaned_data['email'])
		return HttpResponseRedirect('/register/success/')
	else:
		form = RegistrationForm()
		variables = RequestContext(request,{'form'},form)
	return render_to_resonse('registration/register.html',
	variables,
)

def register_success(request):
	return render_to_response('registration/success',)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def home(request):
	return render_to_response('home.html',{'user': request.user})


# Create your views here.
