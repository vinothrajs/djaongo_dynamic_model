"""
URL configuration for erp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from sample import views
from django.contrib import admin
from django.urls import include, path
from sample.employee import  views as employeeviews
from sample.orders.views import add_order_row, order_details, save_orders ,get_price_item,search_results_view

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [  
    path('', views.index),
    path('admin/', admin.site.urls),  

    path('rosetta/', include('rosetta.urls')), #rosetta

    path('__debug__/', include(debug_toolbar.urls)),
    path('home', views.home),  
    path('dynamic_model', views.dynamic_model),  
    path('ajax_view', views.ajax_view), 

    path('employee/', employeeviews.employee_list, name='employee_list'),
    path('employee/add/', employeeviews.employee_create, name='employee_create'),
    path('employee/<int:pk>/', employeeviews.employee_detail, name='employee_detail'),
    path('employee/<int:pk>/update/', employeeviews.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', employeeviews.employee_delete, name='employee_delete'),

    path('addcontact/', views.add_contact, name='add_contact'),
    path('added/', views.contact_added, name='contact_added'),

    path('order-details/', order_details, name='order_details'),
    path('add-order-row/', add_order_row, name='add_order_row'),
    path('save-orders/', save_orders, name='save_orders'),
    path('search/results/', search_results_view, name='search_results_view'),
    path('getprice/<int:item_id>',get_price_item,name='get_price'),
    
    path('i18n/', include('django.conf.urls.i18n')),
    
]  
