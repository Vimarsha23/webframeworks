from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [

	path('', auth_views.LoginView.as_view(template_name = 'registration/login.html'),name = 'login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('card/appointment.html',views.app_new,name = 'app_new'),
	path('card/',views.card , name = "card"),
	path('pedia/appointment.html',views.app_new,name = 'app_new'),
	path('pedia/',views.pedia , name = "pedia"),
	path('gyn/appointment.html',views.app_new,name = 'app_new'),
	path('gyn/',views.gyn , name = "gyn"),
	path('onc/appointment.html',views.app_new,name = 'app_new'),
	path('onc/',views.onc , name = "onc"),
	path('neuro/appointment.html',views.app_new,name = 'app_new'),
	path('neuro/',views.neuro , name = "neuro"),
	path('derm/appointment.html',views.app_new,name = 'app_new'),
	path('derm/',views.derm , name = "derm"),
	path('ent/appointment.html',views.app_new,name = 'app_new'),
	path('ent/',views.ent , name = "ent"),
	path('appointment/',views.app_new,name = 'app_new'),
	path('homepage/',views.homepage,name = 'homepage'),
	#path('', TemplateView.as_view(template_name='homepage.html'), name='home'),
	path('appointment/',views.app_new,name = 'app_new'),
	path('healthtips/',views.health,name = 'health'),
	path('rights/',views.rights,name = 'rights'),
	path('branches/',views.branches,name = 'branches'),
	path('appform/',views.app_form,name = 'app_form'),
	
]
