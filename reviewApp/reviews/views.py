from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	return render(request, 'reviews/home.html', {'title':'Home'})

def about(request):
	return render(request, 'reviews/about.html', {'title':'About Us'})

def contact(request):
	return render(request, 'reviews/contact.html', {'title':'Contact Us'})

def products(request):
	return render(request, 'reviews/products.html', {'title':'Our Products'})

