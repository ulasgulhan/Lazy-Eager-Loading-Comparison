from datetime import datetime
import time
from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
from django.db import connection

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
    start_time = time.time()
    products = Products.objects.all()
    end_time = time.time()
    result = float(end_time) - float(start_time)
    print(f"start time: {start_time}\nEnd time: {end_time}\n{result}")
    return render(request, 'lazy.html', {'products': products})



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
    start_time = time.time()
    products = Products.objects.select_related('supplierid').values("supplierid__companyname").all()
    end_time = time.time()

    result = float(end_time) - float(start_time)
    print(f"start time: {start_time}\nEnd time: {end_time}\n{result}")
    return render (request, 'eager.html', {'products': products})


def index_eager_sql(request):
    start_time = time.time()
    query = """
            select p.ProductName, s.CompanyName from Products as p
            inner join Suppliers as s on p.SupplierID = s.SupplierID
        """
    with connection.cursor() as cursor:
        cursor.execute(query)
        products = cursor.fetchall()

    end_time = time.time()

    result = float(end_time) - float(start_time)
    print(f"start time: {start_time}\nEnd time: {end_time}\n{result}")

    return render(request, 'eager_sql.html', {'products': products})

