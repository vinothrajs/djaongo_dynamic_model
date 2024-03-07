import json
import time
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect  
from .forms import EmployeeForm  
from django.db import models
from django.core.paginator import Paginator
from .models import *

def index(request):  
    return render(request,"index.html",{'object':"index page from py"}) 
def home(request):  
    return render(request,"home.html",{'object':"hello page from py"}) 

## Dynamic Model POC concetpt 1
def get_dynamic_model(table_name, fields):
    app_label_name = 'sample'  # Update with your app label
    module_name = 'sample.models'
    model_name = table_name.lower()  # Assuming table_name is in Title Case

    # Create the dynamic model if not found in cache
    class Meta:
        app_label = app_label_name
        db_table = model_name

    attrs = {
        'Meta': Meta,
        '__module__': module_name  # Update with your app name
    }

    ## dynamic Model creation with relation 
    

    # Iterate over each field in the list
    for metafield in fields:
        field_name = metafield.name
        field_type = metafield.type
        
        # Check if the field type exists in the field_types dictionary
        if field_type in field_types:
            # If the field type exists, use the corresponding model field instance
            attrs[field_name] = field_types[field_type]
        else:
            # If the field type is not found, handle this case accordingly
            print(f"Field type '{field_type}' not supported. Skipping field '{field_name}'")
    # Create the model class
    print(model_name)
    model_class = type(model_name, (models.Model,), attrs)

    return model_class

def dynamic_model(request):
    start_time = time.time()
    # Assume table_name and fields are defined 
    metatables = 'ledger'  # Specify the table name

    metafields = Mfield.objects.filter(table_id=1)

    print(metafields)
    # Get or create the dynamic model
    DynamicModel = get_dynamic_model(metatables, metafields)

    # Perform operations with the dynamic model
    queryset = DynamicModel.objects.all()
    p = Paginator(queryset, 500) 
    page1 = p.page(1000)
    data = serialize("json",  page1.object_list)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time Taken {elapsed_time:.4f} seconds")  
    return JsonResponse(data ,  status=200, safe=False)
    # Now you can use the queryset or perform any other operations with the dynamic model

from django.shortcuts import render
from django.http import JsonResponse

def ajax_view(request):
        context = {
            'message': 'Hello from Ajax!',
            'other_data': 'Some other data you want to pass',
        }
        return render(request, 'ajax_template.html',context)