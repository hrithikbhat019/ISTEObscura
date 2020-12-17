from django.http import HttpRequest
from django.shortcuts import redirect

def user_log_in_required(view_func):
    def wrapper_func(request,*args,**kwargs):
        print(request.session)
        if 'user' in request.session :
            return view_func(request,*args,**kwargs)
        else:
            return redirect('Login')
    return wrapper_func

def only_for_unauthenticated(view_func):
    def wrapper_func(request,*args,**kwargs):
        if 'user' in request.session:
            return redirect('Home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func
