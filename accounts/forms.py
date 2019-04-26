from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ('Name','Gender','dob','age','phone','Email','Speciality')