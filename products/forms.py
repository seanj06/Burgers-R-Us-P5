from django import forms
from .models import Food, Category, SubCategory


class ProductForm(forms.ModelForm):
    """
    Form for superuser to add products
    """
    class Meta:
        model = Food
        exclude = ['sku']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        # Add sub_category field
        sub_categories = SubCategory.objects.all()
        friendly_sub_names = [
            (sc.id, sc.get_friendly_name()) for sc in sub_categories
            ]
        self.fields['sub_category'].choices = friendly_sub_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
