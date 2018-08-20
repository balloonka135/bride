from django import forms
from .models import MailBox, Appointment


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = MailBox
        fields = ['username', 'phone', 'message', 'sender']


class BookAppointForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['username', 'phone', 'message', 'sender', 'date_of_appoint', 'date_of_wedding']
