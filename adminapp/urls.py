from django.urls.conf import path
from . import views

urlpatterns = [
    path('navbar/', views.navbar, name='navbar'),
    path('master/', views.master, name='master'),
    path('adminlogin/', views.fnlogin, name='adminlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/', views.fncustomer, name='customer'),
    path('customerhistory/', views.customerhistory, name='customerhistory'),
    path('editcustomer/<int:id>', views.editcustomer, name='editcustomer'),
    path('viewcustomer/<int:id>', views.viewcustomer, name='viewcustomer'),
    path('fnuser/', views.fnuser, name='user'),
    path('newloan/', views.fnnewloan, name='newloan'),
    path('items/', views.fnitems, name='items'),
    path('itemgroup/', views.fnitemgroup, name='itemgroup'),
    # path('interest/', views.fninterest, name='interest'),
    path('loanhistory/', views.loanhistory, name='loanhistory'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('fnchistory/', views.fnchistory, name='fncustomerhistory'),
    path('suggestname/', views.suggestname, name='suggestname'),
    path('getcustomerdetail/', views.getcustomerdetail, name='getcustomerdetail'),
    path('notifications/', views.notifications, name='notifications'),
    path('addnotification/', views.addnotification, name='addnotification'),
    path('createnotification/', views.createnotification,
         name='createnotification'),
    path('signout/', views.signout, name='signout'),
    path('personalupdate/', views.personalupdate, name='personalupdate'),
    path('contactupdate/', views.contactupdate, name='contactupdate'),
    path('getimage/', views.getimage, name='getimage'),
    path('loadigroup/', views.loadigroup, name='loadigroup'),
    path('loaditems/', views.loaditems, name='loaditems'),
    path('deligroup/', views.deligroup, name='deligroup'),
    path('delitem/', views.delitem, name='delitem'),
    path('delcustomer/', views.delcustomer, name='delcustomer'),
    path('delnotification/<int:id>', views.delnotification, name='delnotification'),
    path('searchcustomer/', views.searchcustomer, name='searchcustomer'),
    path('editadminprofile/', views.editadminprofile, name='editadminprofile'),
    path('getloanamount/', views.getloanamount, name='getloanamount'),
    path('suggestitemgroup/', views.suggestitemgroup, name='suggestitemgroup'),
    path('loaditemgroup/', views.loaditemgroup, name='loaditemgroup'),
    path('suggestitemname/', views.suggestitemname, name='suggestitemname'),
    path('loadvalues/', views.loadvalues, name='loadvalues'),
    path('loadloan/', views.loadloan, name='loadvloan'),
    path('loadloantable/', views.loadloantable, name='loadloantable'),
    path('loaddetails/', views.loaddetails, name='loaddeatils'),
    path('payinterest/', views.payinterests, name='payinterests'),
    path('suggestcustomername/', views.suggestcustomername,
         name='suggestcustomername'),
    path('customerdetails/', views.customerdetails, name='customerdetails'),
]
