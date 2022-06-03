from django.db import models


# New members
class Participants(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    favorite_book = models.CharField(max_length=100)


# Stores information on the existing forms
class FormModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


# Stores html fields
class FormField(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    form = models.ForeignKey(FormModel, on_delete=models.CASCADE)


# Stores the values of the fields
class FormData(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    form_id = models.IntegerField(null=True)
    field_id = models.IntegerField(null=True)
    value = models.CharField(max_length=100)
    record_id = models.IntegerField(null=True)


class FormRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
