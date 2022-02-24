from django.urls.conf import path
from . import views

urlpatterns = [
    path('master/', views.master),
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
    path('interest/', views.fninterest, name='interest'),
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
]
