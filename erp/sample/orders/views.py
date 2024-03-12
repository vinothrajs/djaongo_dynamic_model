import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import OrderDetailForm
from .models import ItemModelSerializer, Items, OrderDetail
from django.core.serializers import serialize

def order_details(request):
    default_order_detail = OrderDetail(quantity=0, price=0.00, ext_price=0.00)
    form = OrderDetailForm(instance=default_order_detail)
    return render(request, 'orders/order_details.html', {'form': form , 'row_count': 1})

def add_order_row(request):
    default_order_detail = OrderDetail(quantity=0, price=0.00, ext_price=0.00)
    form = OrderDetailForm(instance=default_order_detail)
    return render(request, 'orders/order_row.html', {'form': form  , 'counters' : range(2)})
    
def save_orders(request):
    if request.method == 'POST':
        item_names = request.POST.getlist('item_name')
        quantities = request.POST.getlist('quantity')
        prices = request.POST.getlist('price')
        ext_prices = request.POST.getlist('ext_price')
        print(item_names)
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
            else:
                
                data = ItemModelSerializer(form.errors, many=True).data
                return JsonResponse({'Validation': False, 'message': 'Invalid request method' , 'form': data})
           

        try:
            OrderDetail.objects.bulk_create(order_details)
            return JsonResponse({'success': True, 'message': 'Orders saved successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Failed to save orders. Error: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def search_results_view_1(request):
    query = request.GET.get('item_name', '')
    print(f'{query = }')

    all_items = Items.objects.all()
    print(all_items)
    if query:
        matched_item = all_items.filter(item_name__icontains=query)
    else:
        matched_item = []

    context = {'matched_item': matched_item, 'count': all_items.count()}
    print(context)
    return render(request, 'orders/search_results.html', context)

from django.http import JsonResponse
from django.core.serializers import serialize

def search_results_view(request):
    query = request.GET.get("item_name", "")
    print("qi"+query)
    all_items = Items.objects.all()
    print(all_items)
    if query:
        matched_item = all_items.filter(item_name__icontains=query)
    else:
        matched_item = []
    data = ItemModelSerializer(matched_item, many=True).data
    print(matched_item)
    return JsonResponse(data, safe=False)

