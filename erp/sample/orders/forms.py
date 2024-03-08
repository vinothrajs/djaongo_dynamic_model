from django import forms

from.models import OrderDetail

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['item_name', 'quantity', 'price', 'ext_price']
