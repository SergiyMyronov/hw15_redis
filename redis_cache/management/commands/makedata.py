import random

from django.core.management.base import BaseCommand

from redis_cache.models import City, Customer, Product, Supplier


class Command(BaseCommand):
    """
    This command is for inserting City, Customer, Product, Supplier into database.
    Inserts all unique rows to City, Supplier, Product. Then inserts Customers.
    """

    help = 'Making some data'  # noqa

    def handle(self, *args, **kwargs):
        City.objects.all().delete()
        Customer.objects.all().delete()
        Product.objects.all().delete()
        Supplier.objects.all().delete()

        cities = 4  # number of cities and suppliers
        products = 600  # number of products (must be more then cities)
        customers = 12  # number of customers (must be less then products and more then cities)

        cnt = 0
        for c in range(cities):
            city = City.objects.create(name='City'+str(c+1).rjust(2, "0"))
            Supplier.objects.create(name='Supplier'+str(c+1).rjust(2, "0"), city=city, rating=random.randint(2, 5))
            loop = customers // cities
            for i in range(loop):
                Customer.objects.create(name=f'Customer{str(cnt*loop + i + 1).rjust(2, "0")}', city=city)
            cnt += 1

        cnt = 0
        for sup in Supplier.objects.all():
            loop = products // cities
            for i in range(loop):
                Product.objects.create(code=f'Code{str(cnt*loop + i + 1).rjust(3, "0")}',
                                       name=f'Product{str(cnt*loop + i + 1).rjust(3,"0")}',
                                       price=random.randint(200, 900),
                                       weight=random.randint(1, 200),
                                       supplier=sup)
            cnt += 1

        cust_all = list(Customer.objects.all())
        prod_all = list(Product.objects.all())
        len_cust_all = len(cust_all)
        len_prod_all = len(prod_all)
        n = len_prod_all // len_cust_all
        for i in range(len_cust_all):
            for b in range(round(len_cust_all*(1 + random.randint(1, 5) / 10))):
                cust_all[i].products.add(prod_all[random.randint(0, n-2)*len_cust_all+b])
