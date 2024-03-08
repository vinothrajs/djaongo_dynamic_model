from django.shortcuts import render
from django.http import JsonResponse
from .forms import OrderDetailForm
from .models import OrderDetail

def order_details(request):
    initial_form = OrderDetailForm()
    return render(request, 'orders/order_details.html', {'initial_form': initial_form})

def add_order_row(request):
    form = OrderDetailForm()
    return render(request, 'orders/order_row.html', {'form': form})
    
def save_orders_2(request):
    print(request)
    if request.method == 'POST':
        form = OrderDetailForm(request.POST)
        print(form)
        if form.is_valid():
            order_detail = form.save(commit=False)  # Don't save to the database yet
            order_detail.save()  # Save to the database only if the form is valid
            return JsonResponse({'success': True, 'message': 'Order saved successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form data'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def save_orders(request):
    if request.method == 'POST':
        item_names = request.POST.getlist('item_name')
        quantities = request.POST.getlist('quantity')
        prices = request.POST.getlist('price')
        ext_prices = request.POST.getlist('ext_price')

        order_details = []

        for i in range(len(item_names)):
            form_data = {
                'item_name': item_names[i],
                'quantity': quantities[i],
                'price': prices[i],
                'ext_price': ext_prices[i]
            }
            form = OrderDetailForm(form_data)

            if form.is_valid():
                order_details.append(OrderDetail(**form.cleaned_data))

        try:
            OrderDetail.objects.bulk_create(order_details)
            return JsonResponse({'success': True, 'message': 'Orders saved successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Failed to save orders. Error: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})