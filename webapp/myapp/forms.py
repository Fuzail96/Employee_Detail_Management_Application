from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    empid = forms.IntegerField(widget=forms.TextInput(attrs={
        "class":"inp", "placeholder":"Employee Id" }))
    fName = forms.CharField(widget=forms.TextInput(attrs={
        "class": "inp", "placeholder": "First Name"}))
    lName = forms.CharField(widget=forms.TextInput(attrs={
        "class": "inp", "placeholder": "Last Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "inp", "placeholder": "Email"}))
    contact = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "inp", "placeholder": "Contact"}))
    class Meta:
        model = Employee
        fields = "__all__"
