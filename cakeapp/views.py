from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,TemplateView,ListView,UpdateView,DetailView
from cakeapp.forms import RegistrationForm,LoginForm,CategoryCreateForm,CakeAddForm,CakeVarientForm,OfferAddForm
from cakeapp.models import User,CakeCategory,Cakes,CakeVarients,Offers
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

class IndexView(TemplateView):
    template_name="cakeapp/index.html"

class SignUpView(CreateView):
    template_name="cakeapp/register.html"
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("signin")

    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
    
class SignInView(FormView):
    template_name="cakeapp/login.html"
    form_class=LoginForm
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("add-category")
            else:
                messages.error(request,"failed to login")
                return render(request,self.template_name,{"form":form})
 
 
 
class CategoryCreateView(CreateView,ListView):
    template_name="cakeapp/category_add.html"
    form_class=CategoryCreateForm
    model=CakeCategory
    context_object_name="categories"
    success_url=reverse_lazy("add-category")

    def form_valid(self, form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"category adding failed")
        return super().form_invalid(form)
  
def remove_category(request,*args,**kwargs):
    id=kwargs.get("pk")
    CakeCategory.objects.filter(id=id).update(is_active=False)
    messages.success(request,"category is not active")
    return redirect("add-category") 

def active_category(request,*args,**kwargs):
    id=kwargs.get("pk")
    CakeCategory.objects.filter(id=id).update(is_active=True)
    messages.success(request,"category is active")
    return redirect("add-category")


class CakeCreateView(CreateView):
    template_name="cakeapp/cake_add.html"
    model=Cakes
    form_class=CakeAddForm
    success_url=reverse_lazy("cake-list")
    
    def form_valid(self, form):
        messages.success(self.request,"cake added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Failed to add cake")
        return super().form_invalid(form)
    
class CakeListView(ListView):
    template_name="cakeapp/cake_list.html"
    model=Cakes
    context_object_name="cakes"
    
class CakeUpdateView(UpdateView):
    template_name="cakeapp/cake_edit.html"
    form_class=CakeAddForm
    model=Cakes
    success_url=reverse_lazy("cake-list")
    
    def form_valid(self, form):
        messages.success(self.request,"cake updated successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Failed to update cake")
        return super().form_invalid(form)
    
def remove_cakeview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Cakes.objects.filter(id=id).delete()
    return redirect("cake-list")   

class CakeVarientCreateView(CreateView):
    template_name="cakeapp/cakevarient_add.html"
    form_class=CakeVarientForm
    model=CakeVarients
    success_url=reverse_lazy("cake-list")
        
    def form_valid(self,form):
        id=self.kwargs.get("pk")
        obj=Cakes.objects.get(id=id)
        messages.success(self.request,"varient added successfully!")
        form.instance.cake=obj
        return super().form_valid(form)
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        cake_varient_object=CakeVarients.objects.get(id=id)
        cake_id=cake_varient_object.cake.id
        
        return reverse("cake-detail",kwargs={"pk":cake_id})
    
class CakeDetailView(DetailView):
    template_name="cakeapp/cake_detail.html"
    model=Cakes
    context_object_name="cake"
    
class CakeVarientUpdateView(UpdateView):
    template_name="cakeapp/varient_edit.html"
    form_class=CakeVarientForm
    model=CakeVarients
    success_url=reverse_lazy("cake-list")
    
    def form_valid(self, form):
        messages.success(self.request,"varient updated successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Failed to update cake varient")
        return super().form_invalid(form)
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        cake_varient_object=CakeVarients.objects.get(id=id)
        cake_id=cake_varient_object.cake.id
        return reverse("cake-detail",kwargs={"pk":cake_id})
    
def remove_varientview(request,*args,**kwargs):
    id=kwargs.get("pk")
    cake_varient_object=CakeVarients.objects.get(id=id)
    cake_id=cake_varient_object.cake.id
    cake_varient_object.delete()
    return redirect("cake-detail",pk=cake_id) 
    
class OfferCreateView(CreateView):
    template_name="cakeapp/offer_add.html"
    form_class=OfferAddForm
    model=Offers
    success_url=reverse_lazy("cake-list")
    
    def form_valid(self, form):         
        id=self.kwargs.get("pk")
        obj=CakeVarients.objects.get(id=id)
        form.instance.cakevarient=obj
        messages.success(self.request,"offer added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Failed to add offer")
        return super().form_invalid(form)
    
    def get_success_url(self):
        id=self.kwargs.get("pk")
        cakevarientobject=CakeVarients.objects.get(id=id)
        cake_id=cakevarientobject.cake.id
        
        return reverse("cake-detail",kwargs={"pk":cake_id})
    
def remove_offerview(request,*args,**kwargs):
    id=kwargs.get("pk")
    offer_object=Offers.objects.get(id=id)
    cake_id=offer_object.cakevarient.cake.id
    offer_object.delete()
    return redirect("cake-detail",pk=cake_id)   

def signoutview(request,*args,**kwargs):
    logout(request)
    return redirect("signin")