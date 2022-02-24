from django.shortcuts import render
from . models import *
from django.core.files.storage import FileSystemStorage
from random import random
from django.http.response import JsonResponse
from django. db. models import Q
from datetime import date

# Create your views here.


def master(request):
    logid = request.session.get('log')
    print(logid)
    logi = adminLogin.objects.get(id=logid)
    print(logi)
    notify = notification.objects.all().count()
    return JsonResponse({'user': logi.username, 'notify': notify})


def fnlogin(request):
    try:
        if request.method == 'POST':
            username = request.POST['email']
            print(username)
            password = request.POST['password']
            print(password)
            logi_obj = adminLogin.objects.get(
                username=username, password=password)
            request.session['log'] = logi_obj.id

            return render(request, 'dashboard.html')
    except Exception as e:
        print(e)
    return render(request, 'adminlogin.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def fncustomer(request):
    return render(request, 'newcustomer.html')


def fnuser(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            print(name)
            lname = request.POST.get('lname')
            print(lname)
            email = request.POST.get('email')
            print(email)
            password = request.POST.get('password')
            print(password)
            gender = request.POST.get('gender')
            print(gender)
            fathersname = request.POST.get('fname')
            print(fathersname)
            fmobile = request.POST.get('fmobile')
            print(fmobile)
            address1 = request.POST.get('add1')
            print(address1)
            address2 = request.POST.get('add2')
            print(address2)
            city = request.POST.get('city')
            print(city)
            state = request.POST.get('state')
            print(state)
            country = request.POST.get('country')
            print(country)
            pincode = request.POST.get('pincode')
            print(pincode)
            mobile = request.POST.get('mobile')
            print(mobile)
            dob = request.POST.get('dob')
            print(dob)
            furl = request.POST.get('furl')
            print(furl)
            turl = request.POST.get('turl')
            print(turl)
            iurl = request.POST.get('instaurl')
            print(iurl)
            lurl = request.POST.get('lurl')
            print(lurl)
            idproof = request.FILES.get('idproof')
            idproof_name = str(random())+idproof.name
            print(idproof_name)
            resume_obj = FileSystemStorage()
            resume_obj.save(idproof_name, idproof)
            photo = request.FILES.get('photo')
            photo_name = str(random())+photo.name
            print(photo_name)
            photo_obj = FileSystemStorage()
            photo_obj.save(photo_name, photo)
            customer_obj = customer(firstname=name, lastname=lname, gender=gender, fathername=fathersname, fathermobile=fmobile, address1=address1, address2=address2, city=city, mobile=mobile,
                                    state=state, country=country, pincode=pincode, dob=dob, facebookurl=furl, twitterurl=turl, instagramurl=iurl, linkedinurl=lurl, photo=photo_name, idproof=idproof_name, email=email)
            customer_obj.save()
            user_obj = user(email=email, password=password,
                            user_id_id=customer_obj.id)
            user_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'newcustomer.html')


def customerhistory(request):
    return render(request, 'customerhistory.html')


def fnchistory(request):
    user_obj = customer.objects.all()
    user_obje = [{'id': i.id, 'firstname': i.firstname, 'lastname': i.lastname, 'mobile': i.mobile,
                  'email': i.email, 'dob': i.dob, 'city': i.city, 'state': i.state, 'country': i.country} for i in user_obj]
    return JsonResponse({'user': user_obje})


def editcustomer(request, id):
    print(id)
    cus = customer.objects.get(id=id)
    user_obj = user.objects.get(id=id)
    print(cus)

    return render(request, 'editcustomer.html', {'updata': cus, 'user': user_obj})


def viewcustomer(request, id):
    print(id)
    cus = customer.objects.get(id=id)
    user_obj = user.objects.get(id=id)
    print(cus)
    return render(request, 'viewcustomer.html', {'customer': cus, 'user': user_obj})


def fnnewloan(request):
    return render(request, 'newloan.html')


def fnitems(request):
    try:
        if request.method == 'POST':
            itemname = request.POST['item']
            print(itemname)
            item_obj = item(itemname=itemname)
            item_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'items.html')


def fnitemgroup(request):
    try:
        if request.method == 'POST':
            igroup = request.POST['igroup']
            print(igroup)
            itemgroup_obj = itemtype(itemtype=igroup)
            itemgroup_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'itemgroup.html')


def fninterest(request):
    try:
        if request.method == 'POST':
            intype = request.POST['intype']
            print(intype)
            iterest_obj = interest(interesttype=intype)
            iterest_obj.save()
            return JsonResponse({'msg': 'Data added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'interesttype.html')


def loanhistory(request):
    return render(request, 'loanhistory.html')


def forgotpassword(request):
    return render(request, 'forgotpassword.html')


def suggestname(request):
    if 'term' in request.GET:
        search = request.GET.get('term')
        qs = customer.objects.filter(Q(firstname__icontains=search))[0:10]
        print(qs)
        names = list()
        for name in qs:
            names.append(name.firstname)
        return JsonResponse(names, safe=False,)


def getcustomerdetail(request):
    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            print(fname)
            user = customer.objects.get(
                firstname=fname)
            print(user)
            user_obj = [{'id': user.id, 'address': user.address1, 'city': user.city,
                         'state': user.state, 'country': user.country, 'pincode': user.pincode}]
            print(user_obj)
            return JsonResponse({'user': user_obj})
    except Exception as e:
        print(e)


def notifications(request):
    notify = notification.objects.all()
    return render(request, 'notificationlist.html', {'notify': notify})


def addnotification(request):
    return render(request, 'addnotification.html')


def createnotification(request):
    try:
        if request.method == 'POST':
            notify = request.POST['notify']
            print(notify)
            notify_obj = notification(notify=notify)
            notify_obj.save()
            return JsonResponse({'msgs': 'Notification created successfully'})
    except Exception as e:
        print(e)


def signout(request):
    del request.session['log']
    return render(request, 'adminlogin.html')
