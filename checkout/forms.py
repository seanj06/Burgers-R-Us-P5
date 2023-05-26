from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for Order model
    """
    def __init__(self, *args, **kwargs):
        """
        Overides init method setting certain fields to required
        """
        super().__init__(*args, **kwargs)

        required_fields = [
            'full_name', 'email', 'eircode',
            'county', 'town', 'address_1', 'delivery_time'
            ]

        for field in required_fields:
            self.fields[field].required = True

    class Meta:
        """
        Meta class adding required fields and widgets
        """
        model = Order
        fields = [
            'full_name', 'email', 'eircode',
            'county', 'town', 'address_1', 'address_2',
            'address_3', 'delivery_time'
            ]
        widgets = {
            'delivery_time': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'delivery_time': 'Delivery Time',
        }
