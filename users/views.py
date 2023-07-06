from django.shortcuts import render,redirect
# from django.contrib.postgres.
# Create your views here.0
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from users.models import Profile
from django.contrib.auth.models import User
from users.forms import UserUpdateForm,ProfileUpdateForm
def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
        return render(request,'users/register.html',{'form':form})
    if(request.method == 'GET'):
        form = UserRegisterForm()
        return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):  
    if(request.method == 'POST'):
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        # if(p_form.is_valid() || u_form.is_va)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"Your profile is updated successfully")
            redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    context= {
        'u_form':u_form,
        'p_form':p_form 
    }
    return render(request,'users/profile.html',context)