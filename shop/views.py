from audioop import reverse
from django.shortcuts import render
from .models import Feedback, Product, Orders, OrderUpdate, Blogpost, Feedback, Detail, Prepare
from math import ceil
from django.contrib import messages
import json
MERCHANT_KEY = '8Q32lmznhTB4doRNaFl6154a'

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request, 'shop/index.html', {'myposts': myposts})
    
    

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'shop/blogpost.html',
                  {'post':post})
    

def about(request):
    return render(request, 'shop/about.html')




 

def detail(request):
   
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        appointmentdate = request.POST.get('appointmentdate')
        appointmenttime = request.POST.get('appointmenttime')
        message = request.POST.get('message')

        if len(name)<2 or len(phone)<10 or len(appointmentdate)<2 or len(appointmenttime)<2 or len(message)<4: messages.error(request, "Please fill form Correctly")
        else:
            detail = Detail(name=name, phone=phone, appointmentdate=appointmentdate, appointmenttime=appointmenttime, message=message)
            detail.save()
            messages.success(request, "Your Appointment Booked Successfully!")

        

    return render(request, 'shop/detail.html')



def prepare(request):
    if request.method == 'POST':
        yourname = request.POST.get('yourname')
        youremail = request.POST.get('youremail')
        yourphone = request.POST.get('yourphone')
        youraddress = request.POST.get('youraddress') 
        yourcity = request.POST.get('yourcity')
        yourstate = request.POST.get('yourstate')
        postalcode = request.POST.get('postalcode')
        drugname = request.POST.get('drugname')
        potency = request.POST.get('potency')
        quantity = request.POST.get('quantity')

        if len(yourname)<2 or len(yourphone)<10 or len(youremail)<2 or len(yourphone)<2 or len(youraddress)<4: messages.error(request, "please fill form correct")
        else:
            prepare = Prepare(yourname=yourname, youremail=youremail, yourphone=yourphone, youraddress=youraddress, yourcity=yourcity, yourstate=yourstate,  postalcode= postalcode, drugname=drugname, potency=potency, quantity=quantity,) 
            prepare.save()
            messages.success(request, "Order Successfully!")



    return render(request, 'shop/prepare.html')
    


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')



def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False     
    

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'shop/prodView.html', {'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    
        
    else:
        return render(request, 'shop/checkout.html')


def feedback(request):
    if request.method=="POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        comments = request.POST.get('comments', '')

        if len(name)<2 or len(email)<5 or len(comments)<20: messages.error(request, "Please fill form Correctly")
        else:
            feedback = Feedback(name=name, email=email, comments=comments)
            feedback.save()
            messages.success(request, "Order Successfully!") 

    return render(request, 'shop/feedback.html')   
   


   


def product(request):
     # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

   allProds = []
   catprods = Product.objects.values('category', 'id')
   cats = {item['category'] for item in catprods}
   for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
   params = {'allProds':allProds}
   return render(request, 'shop/product.html', params)

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False
