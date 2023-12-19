import time
from django.http import HttpResponse
from django.shortcuts import render
from .models import Categories, Products, Suppliers

# Create your views here.
def index_lazy(request):
    total_time = 0
    num_queries = 10
    for _ in range(num_queries):
        start_time = time.time()
        products = Products.objects.all()
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
    average_time = total_time / num_queries
    print(f"Lazy Loading Average Time: {average_time} seconds")
    return render (request, 'lazy.html', {'products': products})



def index_eager(request):
    total_time = 0
    num_queries = 10
    for _ in range(num_queries):
        start_time = time.time()
        products = Products.objects.select_related('supplierid').all()
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
    average_time = total_time / num_queries
    print(f"Eager Loading Average Time: {average_time} seconds")
    return render (request, 'eager.html', {'products': products})
