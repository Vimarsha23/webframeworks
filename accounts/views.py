from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import AppointmentForm
from django.contrib.auth import views as auth_views

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def homepage(request):
	return render(request,"homepage.html",{})
def derm(request):
	return render(request,"derm.html",{})
def ent(request):
	return render(request,"ent.html",{})
def gyn(request):
	return render(request,"gynic.html",{})
def card(request):
	return render(request,"card.html",{})
def pedia(request):
	return render(request,"pediatricinas.html",{})
def onc(request):
	return render(request,"onc.html",{})
def neuro(request):
	return render(request,"neuro.html",{})
def branches(request):
	return render(request,"contact.html",{})
def rights(request):
	return render(request,"rights.html",{})
def health(request):
	return render(request,"healthtips.html",{})
def app_form(request):
	return render(request,"app_form.html",{})
	
def app_new(request):
	if request.method == "POST":
		form = AppointmentForm(request.POST)
		
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('homepage')
			
	else:
		form = AppointmentForm()
	return render(request, 'post_edit.html', {'form': form})
