from django.urls import path,include
from customer.views import *

urlpatterns = [
    path('get-customer',GetCustomerViews.as_view()),
    path('get-address',GetCustomerViews.as_view()),
    path('get-address',CustomerDetailAddressView.as_view()),

]
