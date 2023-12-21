from datetime import datetime
import time
from django.http import HttpResponse
from django.shortcuts import render
from .models import Categories, Products, Suppliers, OrderDetails

# Create your views here.
def index_lazy(request, id):
    total_time = 0
    num_queries = 10
    for _ in range(num_queries):
        start_time = time.time()
        products = Products.objects.get(pk=id)
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
    average_time = total_time / num_queries
    print(f"Lazy Loading Average Time: {average_time} seconds\nLazy Loading Elapsed Time: {elapsed_time} seconds")
    return render (request, 'lazy_by_id.html', {'products': products})


def index_lazy_all(request):
    total_time = 0
    num_queries = 10
    for _ in range(num_queries):
        start_time = time.time()
        products = Products.objects.all()
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
    average_time = total_time / num_queries
    print(f"Lazy Loading Average Time: {average_time} seconds\nLazy Loading Elapsed Time: {elapsed_time} seconds")
    print(f'{start_time} - {end_time}')
    return render (request, 'lazy.html', {'products': products})



def index_eager(request, id):
    total_time = 0
    num_queries = 10
    for _ in range(num_queries):
        start_time = time.time()
        products = Products.objects.select_related('supplierid').values("supplierid__companyname").get(pk=id)
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
    average_time = total_time / num_queries
    print(f"Eager Loading Average Time: {average_time} seconds\nEager Loading Elapsed Time: {elapsed_time} seconds")
    print(f'{start_time} - {end_time}')
    return render (request, 'eager_by_id.html', {'products': products})


def index_eager_all(request):
    total_time = 0
    num_queries = 10
    for _ in range(num_queries):
        start_time = time.time()
        products = Products.objects.select_related('supplierid').values("supplierid__companyname").all()
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
    average_time = total_time / num_queries
    print(f"Eager Loading Average Time: {average_time} seconds\nEager Loading Elapsed Time: {elapsed_time} seconds")
    print(f'{start_time} - {end_time}')
    print(type(products))
    return render (request, 'eager.html', {'products': products})

