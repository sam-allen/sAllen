from django.shortcuts import render, redirect
from .models import Product, Review
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
	return render(request, 'reviews/home.html', {'title':'Home'})

def about(request):
	return render(request, 'reviews/about.html', {'title':'About Us'})

def contact(request):
	return render(request, 'reviews/contact.html', {'title':'Contact Us'})

class ProductListView(ListView):
	model = Product
	template_name = 'reviews/products.html'
	object_context_name = 'products'
	ordering = ['-name']

class ProductDetailView(DetailView):
	model = Product

class ReviewDetailView(DetailView):
	model = Review
# def products(request):
# 	products_list = {
# 		'products': Product.objects.all()
# 	}

# 	return render(request, 'reviews/products.html', products_list)
