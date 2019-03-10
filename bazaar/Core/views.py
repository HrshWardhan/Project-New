from django.shortcuts import render


def  home (request) :
    if request.user.is_authenticated():
        return render (request,'Core/home2.html')
    else:
        return render(request, 'Core/home.html')

