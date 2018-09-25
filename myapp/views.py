# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm
from django.contrib.auth.models import User
from myapp.models import Book, Author, BookInstance, Genre
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin




class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all() # Get 5 books
    template_name = 'myapp/books.html' 
    paginate_by = 30


def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'myapp/book_detail.html', context={'book': book})

def home_view(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'myapp/homepage.html', context=context)

def user_view(request):
    if request.user.is_authenticated:
        return render(request,'myapp/userpage.html')
    else:
        error = 'Login to continue'
    return render(request,'myapp/loginpage.html',{'error':error})


def userbooks_view(request):
    if request.user.is_authenticated:
        bookinstance_list = BookInstance.objects.filter(borrower=request.user).filter(status__exact='o').order_by('due_back')
        return render(request,'myapp/userbooks.html',{'bookinstance_list':bookinstance_list})
    


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(user_view)
    else:
        form = SignUpForm()
    return render(request,'myapp/signuppage.html',{'form':form})

def login_view(request):
    error = ''
    if request.user.is_authenticated:
            return redirect(user_view)
    if request.method =='POST':
        username = request.POST["username"]
        raw_password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(user_view)
        else:
            error = 'Username or password Incorrect'
    return render(request,'myapp/loginpage.html',{'error':error})

def logout_view(request):
    logout(request)
    return render(request,'myapp/loginpage.html',{})
