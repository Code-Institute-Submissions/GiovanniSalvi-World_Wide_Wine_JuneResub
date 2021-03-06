from django import forms
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'city',
            'postcode',
            'country',
        )

        email = forms.EmailField(required=True, max_length=100)
        