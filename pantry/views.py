from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import razorpay
# Create your views here.

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def index(request):
    return render(request,'index.html')
def products(request):
    data = product.objects.all()
    print(data)
    return render(request, 'product.html', {'data': data})
    return render(request,'product.html')
def service(request):
    return render(request,'service.html')


from .models import *
def register(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = int(request.POST['phno'])
        c = request.POST['email']
        d = request.POST['address']
        e = request.POST['username']
        f = request.POST['password']
        g = request.POST['confirm_password']
        # print(a,b,c,d,e)
        if Register.objects.filter(username=d).exists():
            messages.error(request, 'username already exist')
        else:
            if e == f:
                Register.objects.create(name=a, phone=b, email=c, username=e, password=f).save()
                return HttpResponse("<script>alert('registerd successfully')</script>")
    return render(request, 'register.html')


def log(request):
    if request.method == 'POST':
        a=request.POST['username']
        b=request.POST['password']
        try:
            data=Register.objects.get(username=a)
            if b==data.password:
                request.session['user']=a
                print(request.session['user'])
                return redirect(user_h)
            return HttpResponse('incorrect password')
        except Exception:
            if a=='admin' and b=='1234':
                request.session['admin']=a
                return redirect(admin_h)
            # return redirect('admin_home')-when giving pathname and also add name in urls
            # path('admin_home',views.admin_h,name='admin_home')

            return HttpResponse("invalid username and password")
    return render(request,'login.html')

def admin_h(request):
    if 'admin' in request.session:
         return render(request,'admin_h.html')
    return redirect(log)
def user_h(request):
    if 'user' in request.session:
         return render(request,'user_h.html')
    return redirect(log)
def viewuser(request):
    if 'admin' in request.session:
        d = Register.objects.all()
        return render(request, 'ViewUser_admin.html', {'r': d})
    return render(log)

def addproduct(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            a = request.POST['Product_name']
            b = request.POST['Price']
            c = request.POST['Stock']
            d = request.FILES['img']
            product.objects.create(Product_name=a, Price=b, Stock=c, image=d).save()
            # messages.success(request, 'Data Saved')
        return render(request, 'AddProduct_admin.html')
    return redirect(log)
def manageproduct(request):
    if 'admin' in request.session:
        data=product.objects.all()
        print(data)
        return render(request,'ManageProduct_admin.html',{'data':data})
    return redirect(log)
def delete_product(request,d):
    if 'admin' in request.session:
        data=product.objects.get(pk=d)
        data.delete()
        messages.success(request,'Product deleted Successfully')
        return redirect(manageproduct)
    return redirect(log)
def update_product(request,d):
#     if 'admin' in request.session:
#         data=product.objects.get(pk=d)
#         n = model_form(instance=data)
#         if request.method == 'POST':
#             n = model_form(request.POST, request.FILES,instance=data)
#             if n.is_valid():
#                 n.save()
#                 return HttpResponse('saved')
#         return render(request, 'update_product.html', {'data': n})
#     return render(log)
    if 'admin' in request.session:
        data = product.objects.get(pk=d)
        print(data)
        n = model_form1(instance=data)
        if request.method == 'POST':
            n = model_form1(request.POST, request.FILES, instance=data)
            if n.is_valid():
                n.save()
                messages.success(request, 'product updated succesfully')
                return redirect(manageproduct)

        return render(request, 'update_product.html', {'data': n})
        #     a=re.POST['productname']
        #     b=re.POST['price']
        #     c=re.POST['stock']
        #     products.objects.filter(pk=d).update(productname=a,price=b,stock=c)
        #     return redirect(manageproduct)

    return redirect(log)

def order(request):
    if 'admin' in request.session:
        order = Order.objects.filter(payment_status='PAID').order_by('-purchase_date')
        print(order)
        d1=deliveryboy.objects.all()
        if request.method=='POST':
            a=request.POST['n1']
            b=request.POST['n2']
            c=request.POST['n3']
            d=request.POST['n4']
            e=request.POST['n5']
            f=request.POST['n6']
            # deli=deliveryboy.objects.get(username=a)
            pro=product.objects.get(pk=b)
            ord=Order.objects.get(pk=f)
            print("ord",ord)
            # u=Register.objects.get(username=e)
            print("delivery_id",a,"product_id",b,"quantity",c,"Price",d,"User",e)
            orderitem.objects.create(delivery=a,product_detail=pro,quantity=c,price=d,user_detaill=e,order_details=ord).save()



        return render(request,'OrderDetails_admin.html',{'data': order,'d':d1})
    return redirect(log)
def orderupdate(request,d):
    if 'admin' in request.session:
        ord = Order.objects.get(pk=d)
        e = ord.user.email
        f = ord.product_order
        g = ord.name
        print(g)
        if request.method == 'POST':
            a = request.POST.get('odsts')
            b = request.POST.get('inst')
            Order.objects.filter(pk=d).update(product_status=a, instruction=b)

            send_mail(f'{a}',
                      f'Hey {g},\n\nYour {f} is {a},\n{b} \n\n THANK YOU.',
                      'settings.EMAIL_HOST_USER', [e], fail_silently=False)
            return redirect(order)
        return render(request,'Orederupdate_admin.html',{'data':ord})
    return redirect(log)

def Product(request):
    if 'user' in request.session:
        data = product.objects.all()
        print(data)
        return render(request, 'Products_user.html', {'data': data})
    return render(log)
def display_cart(request):
    if 'user' in request.session:
        # user = register.objects.get(email=re.session['user'])
        data = Register.objects.get(username=request.session['user'])
        cart_items = cart.objects.filter(user_details=data)
        print(cart_items)
        qty = 0
        total = 0
        for i in cart_items:
            qty += i.quantity
            total += i.product_details.Price * i.quantity
        if not cart_items:
            return render(request, 'Cart_user.html')

        return render(request, 'Cart_user.html', {'cart_items': cart_items, 'total': total, 'qty': qty})
    return redirect(log)
def add_cart(request,d):
    if 'user' in request.session:
        u=Register.objects.get(username=request.session['user'])
        p = product.objects.get(pk=d)
        print(p)
        if cart.objects.filter(product_details=p).exists():
              b=cart.objects.get(product_details_id=d)
              print(b)
              b.quantity=b.quantity+1
              print(b.quantity)
              # data = cart_1.objects.create(user_details=a, product_details=b)
              b.save()
              return redirect(display_cart)
        else:

            cart.objects.create(user_details=u,product_details=p).save()
            messages.success(request, 'Item added to cart succesfully')
        return redirect(Product)
    return redirect(log)

# def deletecart(request,d):
#   if 'user' in request.session:
#     data = cart.objects.get(pk=d)
#     data.delete()
#     messages.success(request,'Successfully Deleted')
#     return redirect(cart)

def increment(re,d):
    if 'user' in re.session:
        data=cart.objects.get(pk=d)
        print(data)
        data.quantity+=1
        data.save()
        return redirect(display_cart)
    return redirect(log)
def decrement(re,d):
    if 'user' in re.session:
        data=cart.objects.get(pk=d)
        print(data)
        data.quantity-=1
        data.save()
        return redirect(display_cart)
    return redirect(log)
def wishlist(request):
    if 'user' in request.session:
        data=Register.objects.get(username=request.session['user'])
        d = wish_list.objects.filter(user_details=data)
        print(d)
        return render(request, 'Wishlist_user.html',{'d':d})
    return render(log)


def add_wishlist(request,d):
    if 'user' in request.session:
        u=Register.objects.get(username=request.session['user'])
        p=product.objects.get(pk=d)
        if  wish_list.objects.filter(product_details_id=p).exists():
            messages.success(request,'Item already exists')
        else:
            wish_list.objects.create(user_details=u,product_details=p).save()
            messages.success(request,'Item added to Wishlist Successfully')
        return redirect(Product)
    return redirect(log)

def deletewishlist(request,d):
  if  'user' in request.session:
    data = wish_list.objects.get(pk=d)
    data.delete()
    messages.success(request,'Successfully Deleted')
    return redirect(wishlist)
def deletecart(request,d):
  if  'user' in request.session:
    data = cart.objects.get(pk=d)
    data.delete()
    messages.success(request,'Successfully Deleted')
    return redirect(display_cart)


def myorder(request):
    if 'user' in request.session:
        user = Register.objects.get(username=request.session['user'])
        order = Order.objects.filter(user=user, payment_status='PAID').order_by('-purchase_date')
        return render(request, 'Myorder_user.html', {'data': order})
    return redirect(log)


def profile(request):
    if 'user' in request.session:
        data=Register.objects.get(username=request.session['user'])
        return render(request,'Profile_user.html',{'d':data})
def logout(request):

    return redirect(log)


from .forms import *


def mform(request):
    n=model_form()
    if request.method=='POST':
        n=model_form(request.POST,request.FILES)
        if n.is_valid():
            n.save()
            return HttpResponse('saved')
    return render(request,'model_form.html',{'data':n})

def update_profile(re):
    if 'user' in re.session:
        data=Register.objects.get(username=re.session['user'])
        print(data)
        n=model_form(instance=data)
        if re.method=='POST':
            n=model_form(re.POST,re.FILES,instance=data)
            if n.is_valid():
                n.save()
                return redirect(profile)
        return render(re,'update_profile.html',{'data':n})

def payment(request,l,d,k):
    pro = product.objects.get(pk=d)
    amount = l * 100
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    if pro.Stock >=1:
        product.objects.filter(pk=pro.id).update(Stock =pro.Stock-k)
    # status='PAID'
    # Order.objects.filter(pk=v).update(payment_status=status)
    return render(request, "payment.html",{'amount':amount})


def paymentsuccess(request):
    user=Register.objects.get(username=request.session['user'])
    a = request.session['order_id']
    print(a)
    b = 'PAID'
    c = request.session['order_name']
    print(c)
    Order.objects.filter(pk=a).update(payment_status=b)
    # send_mail('Payment Successful',
    #           f'Hey {user.name}, Your payment was successful and order for {c} has been successfully placed. \nWe are working on your order. \nOrder status will be updated soon.\n\nTHANK YOU.. \n\nBest regards,\nGAMER ZONE',
    #           'settings.EMAIL_HOST_USER', [user.email], fail_silently=False)
    # send_mail('New Order',
    #           f' {user.name}, has placed a new order for {c}\nPlease review and update the order status',
    #           'settings.EMAIL_HOST_USER', ['gmrznadmn@gmail.com'], fail_silently=False)
    return render(request, "paymentsuccess.html")

def paymentcart(request,l,d):
    data=cart.objects.get(pk=d)
    data.delete()
    amount = l * 100
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, "paymentcart.html",{'amount':amount})

def paymentsuccess_cart(request):
    usr = Register.objects.get(username=request.session['user'])
    order_ids = request.session.get('order_ids', [])
    for i in order_ids:
        c = i
        b = 'PAID'
        Order.objects.filter(pk=c).update(payment_status=b)
    # send_mail('Payment Successful',
    #           f'Hey {usr.name}, Your payment was successful and your ordered items has been successfully placed. \nWe are working on your order. \nOrder status will be updated soon.\n\nTHANK YOU.. \n\nBest regards,\nGAMER ZONE',
    #           'settings.EMAIL_HOST_USER', [usr.email], fail_silently=False)
    # send_mail('New Order',
    #           f' {usr.name}, has placed a some new orders\nPlease review and update the order status',
    #           'settings.EMAIL_HOST_USER', ['aninaabraham01@gmail.com'], fail_silently=False)
    return render(request, "paymentsuccess.html")
def checkout(request,d):
    # user = register.objects.get(email=request.session['user'])
    data = Register.objects.get(username=request.session['user'])
    pro = product.objects.get(pk=d)

    if request.method=='POST':
        a = request.POST['chname']
        print(a)
        c = request.POST.get('chaddress')
        m = request.POST.get('chcity')
        e = request.POST.get('chstate')
        f = request.POST.get('chcountry')
        g = request.POST.get('chzipcode')
        h = request.POST.get('chphone')
        k = int(request.POST.get('chqty'))
        l = int(request.POST.get('chtotal'))

        if pro.Stock >= 1:
            val = Order.objects.create(user=data, name=a, address=c, city=m, state=e, country=f, zip_code=g, phone=h, product_order=pro, quantity=k, total_price=l)
            val.save()
            request.session['order_name']= pro.Product_name
            request.session['order_id'] = val.pk

            return redirect(payment,l,d,k)
        else:
            messages.error(request,'Low Stock')
            return redirect(Product)
    return render(request, 'checkout.html',{'data':pro, 'user':data})

def checkoutcart(request,total,qty):
    # user = register.objects.get(email=request.session['user'])
    data = Register.objects.get(username=request.session['user'])
    pro=cart.objects.filter(user_details=data)

    order_ids = []
    if request.method == 'POST':
        a = request.POST.get('chname')
        c = request.POST.get('chaddress')
        d = request.POST.get('chcity')
        e = request.POST.get('chstate')
        f = request.POST.get('chcountry')
        g = request.POST.get('chzipcode')
        h = request.POST.get('chphone')
        l = int(request.POST.get('chtotal'))
        print("Pro", pro)
        for i in pro:
            print("Productt",i)
            cn = i.product_details
            cq = i.quantity
            ct = i.product_details.Price * i.quantity
            print(cn,cq,ct)
            v=Order.objects.create(user=data, name=a, address=c, city=d, state=e, country=f, zip_code=g, phone=h, product_order=cn,quantity=cq,total_price=ct)
            v.save()
            value1 = v.pk
            order_ids.append(value1)
            if i.product_details.Stock >=1:
                product.objects.filter(pk=i.product_details.pk).update(Stock=i.product_details.Stock-cq)
                request.session['order_ids'] = order_ids
                print("i",i)
                return redirect(paymentcart, l,i.pk)
            else:
                messages.error(request,'Low Stock')
                return redirect(display_cart)
    return render(request,'checkout_cart.html',{'user':data,'data':pro,'total':total,'qty':qty})
def mail(request):
    m = request.POST['mail']
    data =Mail.objects.create(mail=m)
    data.save()
    # send_mail('Subscribed',
    #           f'Welcome to GAMERZONE\n Your email has been successfully registered for our newsletters\nWe will notify you about the latest products and updates\n\nTHANK YOU.. \n\nBest regards,\nGAMER ZONE',
    #           'settings.EMAIL_HOST_USER', [m], fail_silently=False)
    return render(request,'user_h.html')

def userrecentorders(request):
    if 'user' in request.session:
        user = Register.objects.get(username=request.session['user'])
        order = Order.objects.filter(user=user,payment_status='PAID').order_by('-purchase_date')
        return render(request, 'Myorder_user.html',{'data':order})
    return redirect(log)
def adminrecentorders(request):
    if 'admin' in request.session:
        order = Order.objects.filter(payment_status='PAID').order_by('-purchase_date')
        print(order)

        return render(request,'OrderDetails_admin.html',{'data': order})
    return redirect(log)

def lowstock(request):
    if 'admin' in request.session:

        pro = product.objects.all()
        l = []
        for i in pro:
            print(i.Stock)

            if i.Stock <= 3:
                l.append(i)
                # d=products.objects.filter(productname=i.productname)
                # print(d)
                return redirect(lowstock)

    return render(request, 'lowstock.html', {'e': l})

from django.utils.crypto import get_random_string
from django.core.mail import send_mail
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Register.objects.get(email=email)
        except:
            messages.info(request, "Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}',
                      'settings.EMAIL_HOST_USER', [email], fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request, "Network connection failed")
            return redirect(forgot_password)

    return render(request,'forgot.html')
def reset_password(request,token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    # usr = User.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            password_reset.user.password=new_password
            password_reset.user.save()
            # password_reset.delete()
            return redirect(log)
    return render(request, 'reset_password.html', {'token': token})

def adminuser(request):
    if 'admin' in request.session:
        order = Order.objects.filter(payment_status='PAID',product_status='Order Placed')
        order1 = Order.objects.filter(payment_status='PAID',product_status='Preparing')
        order2 = Order.objects.filter(payment_status='PAID',product_status='Packing')
        order3 = Order.objects.filter(payment_status='PAID',product_status='Ready For Delivery')
        order4 = Order.objects.filter(payment_status='PAID',product_status='Out For Delivery')
        return render(request,'admin_user.html',{'data':order,'data1':order1,'data2':order2,'data3':order3,'data4':order4})
    return redirect(log)
def adminorderupdate(request,d):
    if 'admin' in request.session:
        ord = Order.objects.get(pk=d)
        e = ord.user.email
        f = ord.product_order
        g = ord.name
        print(g)
        if request.method == 'POST':
            a = request.POST.get('odsts')
            b = request.POST.get('inst')
            c = request.POST.get('setTodaysDate')
            Order.objects.filter(pk=d).update(product_status=a, instruction=b,delivery_date=c)

            send_mail(f'{a}',
                      f'Hey {g},\n\nYour {f} is {a},\n{b} \n\n THANK YOU.',
                      'settings.EMAIL_HOST_USER', [e], fail_silently=False)
            return redirect(order)
        return render(request,'Orderupdate_admin.html',{'data':ord})
    return redirect(log)


def dbregister(re):

    if re.method == "POST":
        a =re.POST['name']
        b = int(re.POST['phno'])
        c = re.POST['email']
        d =re.POST['username']
        e =re.POST['password']
        f =re.POST['confirmpassword']
        g=re.FILES['proof']
        if e==f:
          data= deliveryboy.objects.create(name=a,phno=b,email=c,username=d,password=f,proof=g)
          data.save()
          return HttpResponse("<script>alert('registration successfull')</script>")
        else:
            return HttpResponse('doesnot exist ')

    return render(re, "dbregister.html")

def dblogin(re):
    if re.method == "POST":
        d = re.POST['username']  # to get data
        e = re.POST['password']
        try:
            data = deliveryboy.objects.get(username=d)  # to get the username
            print(data)
            if e == data.password:
                if data.status == 'accept':
                    re.session['db'] = d
                    print(re.session['db'])
                    print(data.password)  # password field
                    # return HttpResponse("<script>alert('login successfully')</script>")
                    return redirect(dbhome)
            return HttpResponse("Password Incorrect")  # work as else

        except Exception:
            # if d == 'admin' and e == '1234':
            #     re.session['admin'] = d
            #     return redirect(adminhome)
            # else:
            return HttpResponse("invalid username and password for db")
    else:
        return render(re, 'dblogin.html')

def dbhome(re):
    if 'db' in re.session:
       return render(re,'dbhome.html')
    return redirect(dblogin)

def dbprofile(request):
    if 'db' in request.session:
        data = deliveryboy.objects.get(username=request.session['db'])
        return render(request, 'dbprofile.html', {'d': data})
    return redirect(dblogin)


def dborderdetails(request):
    if 'db' in request.session:
        deli=deliveryboy.objects.get(username=request.session['db'])
        print("deli",deli)
        order = orderitem.objects.filter(delivery=deli.username)
        print(order)
        # orderitem.objects.filter(username=order.user_detaill).update(status='delivered')
        # messages.success(request, 'Order delivered')
        return render(request,'dborderdetails.html',{'data': order})
    return redirect(dblogin)

def viewdb(request):
    if 'admin' in request.session:
        d = deliveryboy.objects.all()
        return render(request, 'ViewDb_admin.html', {'r': d})
    return render(dblogin)

def update_db(re):
    if 'user' in re.session:
        data=deliveryboy.objects.get(username=re.session['db'])
        print(data)
        n=model_form2(instance=data)
        if re.method=='POST':
            n=model_form2(re.POST,re.FILES,instance=data)
            if n.is_valid():
                n.save()
                return redirect(dbprofile)
        return render(re,'update_db.html',{'data':n})
    return render(dblogin)
def Reject(request,d):
    if 'admin' in request.session:
        data = deliveryboy.objects.get(pk=d)
        print(data)
        data.status = 'reject'
        data.work_status = 'reject'
        data.save()
        messages.success(request, 'Request Rejected')
        return redirect(viewdb)
        # return render(request, 'ViewDb_admin.html', {'data': n})
    return redirect(log)
def Accept(request,d):
    if 'admin' in request.session:
        data = deliveryboy.objects.get(pk=d)
        print(data)
        data.status='accept'
        data.save()
        messages.success(request, 'Request Accepted')
        return redirect(viewdb)
        # return render(request, 'ViewDb_admin.html', {'data': n})
    return redirect(log)

# def dborderupdate(request,d):
#     if 'db' in request.session:
#         ord = orderitem.objects.get(pk=d)
#         e = ord.user_detaill
#         f = ord.product_detail
#         g = ord.delivery
#         print(g)
#         if request.method == 'POST':
#             a = request.POST.get('odsts')
#             b = request.POST.get('inst')
#             Order.objects.filter(pk=d).update(product_status=a, instruction=b)
#
#             send_mail(f'{a}',
#                       f'Hey {g},\n\nYour {f} is {a},\n{b} \n\n THANK YOU.',
#                       'settings.EMAIL_HOST_USER', [e], fail_silently=False)
#             return redirect(dborderdetails)
#         return render(request,'db_order_update.html',{'data':ord})
#     return redirect(dblogin)

def accept_db(request,d):
    if 'db' in request.session:
        data = orderitem.objects.get(pk=d)
        deliveryboy.objects.filter(username=data.delivery).update(work_status='busy')
        print(data.user_detaill)
        data.status='accept'
        data.save()
        messages.success(request, 'Accepted the order')
        return redirect(dborderdetails)
    return redirect(dblogin)

def reject_db(request,d):
    if 'db' in request.session:
        data = orderitem.objects.get(pk=d)
        print(data)
        data.status = 'reject'
        data.save()
        messages.success(request, 'Request Rejected')
        return redirect(dborderdetails)
        # return render(request, 'ViewDb_admin.html', {'data': n})
    return redirect(dblogin)


def delivered_update(request,d):
    if 'db' in request.session:
        data = orderitem.objects.get(pk=d)
        print("user",data.delivery)
        deliveryboy.objects.filter(username=data.delivery).update(work_status='free')
        print(data)
        data.status = 'delivered'
        data.save()
        messages.success(request, 'Delivered Successfully')
        return redirect(dborderdetails)
    return redirect(dblogin)