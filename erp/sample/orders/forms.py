from django import forms

from.models import OrderDetail

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['item_name', 'quantity', 'price', 'ext_price']
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 0:
            raise forms.ValidationError("Quantity cannot be less than zero.")
        return quantity