from django.views import View
from django.shortcuts import render, redirect

from .forms import RegistrationForm
from .models import Participants, FormField, FormData


class MainView(View):
    def get(self, request):
        # Get all data from the database
        query_results = Participants.objects.all()

        # Get all fields from the database
        fields = FormField.objects.all()

        # Get all data from the database
        data = FormData.objects.all()

        # Render the template
        return render(request, 'index.html', {'query_results': query_results, 'fields': fields, 'data': data})


class RegisterView(View):
    def post(self, request):
        # Get data from form
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Create new entry for every field in the registration form
            for field in FormField.objects.all():
                # Create new entry in the database
                new_entry = FormData(field_id=field.id, value=request.POST[field.name])
                new_entry.save()

            return redirect("/")

    def get(self, request):
        participants = FormField.objects.all()

        return render(request, "register.html", {'participants': participants})
