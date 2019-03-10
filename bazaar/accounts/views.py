
from django.shortcuts import render,redirect
from .forms  import RegistrationForm,EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def  Login (request) :
    return render (request,'accounts/login.html')
def  register(request):
    if request.method == 'POST':
        f = RegistrationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('register')

    else:
        f = RegistrationForm()

    return render(request, 'accounts/reg_form.html', {'form': f})


def profile(request):
    args = {'user': request.user}
    return render (request, 'accounts/profile.html', args)


def profileedit(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request,'accounts/edit_profile.html', args)

def changepassword(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/account/profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request,'accounts/passwordchange.html', args)