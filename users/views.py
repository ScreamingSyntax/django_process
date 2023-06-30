from django.shortcuts import render,redirect
# from django.contrib.postgres.
# Create your views here.0
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
            # return render(request,'users/register.html',{'form':form})
        return render(request,'users/register.html',{'form':form})
        # else:
        #     errors = form.error_messages.items
        #     error_message = ''
        #     print(errors)
        #     # for error in errors:
        #     #     error_message=error
        #         # print(err)
        #     messages.warning(request,f'You have an error {error_message}')
        #     return redirect('register')
    if(request.method == 'GET'):
        form = UserRegisterForm()
        return render(request,'users/register.html',{'form':form})

    # if(request == 'POST'):
    # else:
    #     return render(request,'users/register.html')