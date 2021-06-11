from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import Userregistarions

@login_required
def index(request):
    print(request)
    return render(request, 'user/index.html')

def register(request):
    if request.method == 'POST':
        form = Userregistarions(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You log in')
            return redirect('index')


    else:
        form = Userregistarions()

    return render(request, 'user/register.html', {'form': form})