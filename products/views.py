from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import product_form
from django.contrib.auth.decorators import login_required

@login_required
def products_view(request):
    objs=Product.objects.get(id=16)
    context={
        'title' :objs.title,
        'description': objs.description
    }

    return render(request, "products_details.html", context)
@login_required
def all_products(request):
    all_products=Product.objects.all().order_by('title')
    context={
        'all_products': all_products,
    }
    return render (request, 'all_products.html', context)
@login_required
def product_create(request):
    if request.method=='POST':
        form=product_form(request.POST or None)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            msg = 'saved successful'
            messages.add_message(request, messages.INFO, msg)
            context={
            'form': form,
        }
            
            return render(request, 'product_create.html', context)

    else:
        form=product_form()
        context={
            'form': form
        }

        return render(request, 'product_create.html', context)

@login_required
def product_update(request, id):
    objct=get_object_or_404(Product, id=id)
    if request.method=='POST':
        form=product_form(request.POST, instance=objct)
        if form.is_valid():
            Product.objects.filter(pk=id).update_or_create(**form.cleaned_data)
            context={
                'form':form
            }
            return render(request, 'product_update.html', context)

    else:
        form=product_form(instance=objct)
        context={
            'form': form
        }
        return render(request, 'product_update.html', context)

@login_required
def delete_product(request, id):
    objct=Product.objects.get(id=id)
    objct.delete()
    return redirect('products:all_products')
    all_products=Product.objects.all()
    context={
        'all_products':all_products
    }
    return render(request, 'all_products.html', context)

     
from django.http import Http404
@login_required
def product_url(request, id):
    try:
        obj=Product.objects.get(id=id)
        context={
            'objects': obj
        }
        return render(request, 'products_details.html', context)
    except Product.DoesNotExist:
        raise Http404("product does not exist")

    return render(request, 'products_details.html', context)