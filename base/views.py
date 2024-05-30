from django.shortcuts import render,redirect
from .models import Category,Product
from .forms import ProductForm
from django.http import HttpResponse
from django.db.models import Q

def getAllProducts(request):
    q=request.GET.get('q')
    allproducts=Product.objects.filter(
        Q(category__name__icontains=("" if q==None else q)) |
        Q(name__icontains=("" if q==None else q))
    )
    productscount=len(allproducts)
    allcategory=Category.objects.all()
    context={'allproducts':allproducts,'productscount':productscount,'allcategory':allcategory}
    return render(request,'base/home.html',context)

def getProductbyId(request,pk):
    product=Product.objects.get(id=pk)
    context={'product':product}
    return render(request,'base/getproduct.html',context)

def create_product(request):
    form=ProductForm()
    if(request.method=='POST'):
        form=ProductForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('allproduct')
    context={'form':form}
    return render(request,'base/product_form.html',context)

def update_product(request,pk):
    getproduct=Product.objects.get(id=pk)
    form=ProductForm(instance=getproduct)
    context={'form':form}
    if(request.method=='POST'):
        form=ProductForm(request.POST,instance=getproduct)
        if(form.is_valid()):
            form.save()
            return redirect('allproduct')
    return render(request,'base/product_form.html',context)

def deleteproduct(request,pk):
    product=Product.objects.get(id=pk)
    if(request.method=="POST"):
        product.delete()
        return redirect('allproduct')
    return render(request,'base/delete.html',{'obj':product})
