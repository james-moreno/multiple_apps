from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Register

# Create your views here.
def index(request):
    return render(request, "landr/index.html")

def register(request):
    if request.method=="POST":
        reg_data = Register.objects.new_reg(request.POST)
        if reg_data['created']:
            messages.success(request, "{} successfully registered".format(reg_data['new_user'].first_name))
        else:
            for error in reg_data['errors']:
                messages.error(request, error)
    return redirect(reverse('landr:index'))

def login(request):
    if request.method=="POST":
        log_data = Register.objects.login(request.POST)
        if log_data['log_in']:
            messages.success(request, "Success! Welcome {}".format(log_data['user'].first_name))
            return render(request, "landr/success.html")
        else:
            for error in log_data['errors']:
                messages.error(request, error)
            return redirect(reverse('landr:login'))
