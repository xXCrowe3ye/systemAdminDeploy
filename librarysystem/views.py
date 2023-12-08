from django.shortcuts import render,redirect
from django import contrib
from .forms import *
from django.contrib import messages
from .models import booklib
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}.")
            return redirect('login_view')  # Redirect to the login page after successful registration
        else:
            return render(request, 'register.html', {'error_message': 'Invalid credentials'})     
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def index(request):    
    return render(request,'index.html', {})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        try:
            user = User.objects.get(username=username)
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login_view.html', {'error_message': 'Invalid credentials'})
        except User.DoesNotExist:
            return render(request, 'login_view.html', {'error_message': 'User does not exist'})
    else:
        return render(request, 'login_view.html', {})

def addbooks(request):
    if request.method == "POST":
        form = booklibForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('globalLib')
    else:
        form = booklibForm()

    return render(request, 'addbooks.html', {'form': form})

def globalLib(request):    
    books = booklib.objects.all()
    return render(request, 'globalLib.html', {'books': books})

def search(request):
    query = request.GET.get('query')
    data = booklib.objects.filter(bookgenre__icontains=query)
    context = {'data': data, 'query': query}
    return render(request, 'globalLib.html', context)

def display_file(request, book_id):
    book = booklib.objects.get(pk=book_id)
    return render(request, 'globalLib.html', {'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(booklib, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('globalLib')  # Replace 'globalLib' with the name of the URL pattern for your globalLib page
    return render(request, 'globalLib.html', {'book': book})