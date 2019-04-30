from django.shortcuts import render, redirect
from .models import Product
from .forms import product_form

def products_view(request):
    objs=Product.objects.get(id=16)
    context={
        'title' :objs.title,
        'description': objs.description
    }

    return render(request, "products_details.html", context)

def all_products(request):
    all_products=Product.objects.all()
    context={
        'all_products': all_products,
    }
    return render (request, 'all_products.html', context)

def product_create(request):
    if request.method=='POST':
        form=product_form(request.POST or None)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            context={
            'form': form
        }
            return render(request, 'product_create.html', context)

    else:
        form=product_form()
        context={
            'form': form
        }

        return render(request, 'product_create.html', context)
def delete_product(request, id):
    objct=Product.objects.get(id=id)
    objct.delete()
    return redirect('products:all_products')
    all_products=Product.objects.all()
    context={
        'all_products':all_products
    }
    return render(request, 'all_products.html', context)

     

def product_url(request, id):
    obj=Product.objects.get(id=id)
    context={
        'objects': obj
    }
    return render(request, 'products_details.html', context)

