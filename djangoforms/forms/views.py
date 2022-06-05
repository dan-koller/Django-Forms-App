from django.views import View
from django.shortcuts import render, redirect

from .forms import RegistrationForm
from .models import Participants, FormField, FormData


class MainView(View):
    def get(self, request):
        # Get all data from the database
        results = Participants.objects.all()

        # Get all fields from the database
        fields = FormField.objects.all()

        # Get all form data from the database
        data = FormData.objects.all()

        # Render the template
        return render(request, 'index.html', {'results': results, 'fields': fields, 'data': data})


class RegisterView(View):
    def post(self, request):
        # Get data from form
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Create new entry for every field in the registration form
            for field in FormField.objects.all():
                new_entry = FormData(field_id=field.id, value=request.POST[field.name])
                new_entry.save()

            # Create new participant entry
            new_participant = Participants(name=request.POST["name"], age=request.POST["age"],
                                           favorite_lang=request.POST["favorite_lang"],
                                           birthday=request.POST["birthday"])
            new_participant.save()

            return redirect("/")
        else:
            # Print field errors to console
            for f in form:
                print("Field Error:", f.name, f.errors)

    def get(self, request):
        participants = FormField.objects.all()

        return render(request, "register.html", {'participants': participants})
