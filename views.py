from django.shortcuts import render,redirect
from .models import*
from c_app.models import*
from django.db.models.aggregates import Sum
# Create your views here.
def user_index(request):
    data=chemical.objects.all()
    return render(request,'user_index.html',{'data':data,})
def user_login(request):
    name1=request.POST.get('name')
    password1=request.POST.get('password')
    if Register.objects.filter(name=name1,password=password1).exists():
        data=Register.objects.filter(name=name1,password=password1).values('name','email','phone','id').first()
        request.session['uname']=data['name']
        request.session['uemail']=data['email']
        request.session['uphone']=data['phone']
        request.session['name']=name1
        request.session['password']=password1
        request.session['id']=data['id']
        return redirect('user_index')
    else:
        return render(request,'user_login.html')
def getdata2(request):
    if request.method=="POST":
        name1=request.POST['name']
        pass1=request.POST['password']
        email1=request.POST['email']
        phone1=request.POST['phone']
        data=Register(name=name1,password=pass1,email=email1,phone=phone1)
        data.save()
        return redirect('user_registration')
def user_registration(request):
    return render(request,'user_registration.html')
def user_logout(request):
    del request.session['uname']
    del request.session['uemail']
    del request.session['uphone']
    del request.session['name']
    del request.session['password']
    del request.session['id']
    return redirect('user_index')
def product(request,id):
    data=chemical.objects.filter(id=id)
    return render(request,'product.html',{'data':data,})
def quantity(request):
    return render(request,'quantity.html')
def cartdata(request,pid):
    if request.method=="POST":
        quantity=request.POST.get('quan')
        total=request.POST.get('total')
        userid=request.session.get('id')
        data=Cart(productid=chemical.objects.get(id=pid),quantity=quantity,total=total,userid=Register.objects.get(id=userid),status=0)
        data.save()
    return redirect('cart')
def cart(request):
    userid=request.session.get('id')
    data=Cart.objects.filter(userid=userid,status=0)
    s =  Cart.objects.filter(userid=userid,status=0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'s':s})
def contact(request):
    return render(request,'contact.html')
def con_data(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        sub1=request.POST['subject']
        msg=request.POST['message']
        data=Contact(name=name1,email=email1,subject=sub1,message=msg)
        data.save()
        return redirect('contact')   

def delete1(request,id):
    Cart.objects.filter(id=id).delete()
    return redirect('cart')

def checkout(request):
    userid = request.session.get('id')
    data=Cart.objects.filter(userid=userid,status=0)
    s =  Cart.objects.filter(userid=userid,status=0).aggregate(Sum('total'))
    print(s)
    return render(request,'checkout.html',{'data':data,'s':s})

def checkoutdata(request):
    if request.method=="POST":
        address1=request.POST['address']
        state1=request.POST['state']
        country1=request.POST['country']
        district1=request.POST['district']
        zip1=request.POST['postal_zip']
        u=request.session['id']
        order=Cart.objects.filter(userid=u,status=0)
        for i in order:
            data = Checkout(userid=Register.objects.get(id=u),cartid=Cart.objects.get(id=i.id),address=address1,country=country1,state=state1,district=district1,postal_zip=zip1)
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
    return redirect('user_index')
