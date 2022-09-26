from django import forms
from .models import EventMember


class RegisterForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ['full_name', 'email', 'phone', 'event']

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if (full_name == ""):
            raise forms.ValidationError(
                " Sorry, Your name cannot be empty! Please")

        return full_name



    def clean_email(self):
        email = self.cleaned_data.get('email')
        event = self.cleaned_data.get('event')

        if (email == ""):
            raise forms.ValidationError(" Sorry, Your email cannot be empty!")
        for instance in EventMember.objects.all():
            if (instance.email == email and instance.event == event):
                raise forms.ValidationError(
                    " You already registered with this email ")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        event = self.cleaned_data.get('event')

        if (phone == ""):
            raise forms.ValidationError(" Sorry, Your email cannot be empty!")
        for instance in EventMember.objects.all():
            if (instance.phone == phone and instance.event == event):
                raise forms.ValidationError(
                    " You already registered with this phone ")
        return phone

    def clean_event(self):
        event = self.cleaned_data.get('event')
        
        if (event == ""):
            raise forms.ValidationError(" You have to choose an event ")
        for instance in EventMember.objects.all():
            if (instance.event == event):
                eve = EventMember.objects.filter(event=instance.event).count()
                if (instance.event.maximum_attende <= eve):
                    raise forms.ValidationError("seats are full")
        return event

