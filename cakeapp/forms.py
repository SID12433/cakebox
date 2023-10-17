from django import forms
from cakeapp.models import User,CakeCategory,Cakes,CakeVarients,Offers
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","phone","address"]      
        
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model=CakeCategory
        fields=["name"]
        
class CakeAddForm(forms.ModelForm):
    class Meta:
        model=Cakes
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"})
        }

class CakeVarientForm(forms.ModelForm):
    class Meta:
        model=CakeVarients
        exclude=("cake",)
        
class OfferAddForm(forms.ModelForm):
    class Meta:
        model=Offers
        exclude=("cakevarient",)
          
        widgets={
            "start_date":forms.DateInput(attrs={"type":"date"}),
            "due_date":forms.DateInput(attrs={"type":"date"})
        }
   
    
