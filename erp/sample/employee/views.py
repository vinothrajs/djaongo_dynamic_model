from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator

def employee_list(request):
    # employees = Employee.objects.all()
    # p = Paginator(employees, 500) 
    # page1 = p.page(1000)
    employees1 = Employee.objects.all()
    # p1 = Paginator(employees1, 2000) 
    # page11 = p1.page(500)
    return render(request, 'employees/employee_list.html', {'employees': employees1})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

def employee_create(request):
    field_config = [
        {'name': 'eid', 'type': 'char', 'max_length': 2, 'required': True},
        {'name': 'ename', 'type': 'char', 'max_length': 2, 'required': True},
        {'name': 'eemail', 'type': 'email', 'required': True},
        {'name': 'econtact', 'type': 'char', 'max_length': 2, 'required': True}
    ]  # Example field configuration list
    if request.method == 'POST':
        form = EmployeeForm(field_config,request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(field_config)
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_update(request, pk):
    
    employee = get_object_or_404(Employee, pk=pk)
    field_config = [
            {'name': 'eid', 'type': 'char', 'max_length': 2, 'required': True},
            {'name': 'ename', 'type': 'char', 'max_length': 2, 'required': True},
            {'name': 'eemail', 'type': 'email', 'required': True},
            {'name': 'econtact', 'type': 'char', 'max_length': 2, 'required': True}
        ]  # Example field configuration list
        
    
    if request.method == 'POST':

        form = EmployeeForm(field_config, request.POST ,instance=employee)
        print(form)
        if form.is_valid():
            print("formsaved")
            form.save()
            return redirect('employee_list')
        else:
            print("not valid")
            return render(request, 'employees/employee_form.html', {'form': form})
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
