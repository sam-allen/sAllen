from django.shortcuts import render, redirect
from .models import Product, Review
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ReviewCreateView(LoginRequiredMixin, CreateView):
	model = Review
	fields = ['product','rating', 'review_text', 'date']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
