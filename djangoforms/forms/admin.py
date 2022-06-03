from django.contrib import admin
from .models import Participants, FormModel, FormField, FormData


# Register your models here.
class ParticipantsAdmin(admin.ModelAdmin):
    pass


class FormModelAdmin(admin.ModelAdmin):
    pass


class FormFieldAdmin(admin.ModelAdmin):
    pass


class FormDataAdmin(admin.ModelAdmin):
    pass


class FormRecordAdmin(admin.ModelAdmin):
    pass


# Register admins
admin.site.register(Participants, ParticipantsAdmin)
admin.site.register(FormModel, FormModelAdmin)
admin.site.register(FormField, FormFieldAdmin)
admin.site.register(FormData, FormDataAdmin)
