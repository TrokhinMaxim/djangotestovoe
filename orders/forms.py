from django import forms
from itertools import product

from robots.models import POSSIBLE_MODELS, POSSIBLE_VERSIONS

available_combinations = list(product(POSSIBLE_MODELS, POSSIBLE_VERSIONS))
available_serials = ["-".join(combination) for combination in available_combinations]


class OrderForm(forms.Form):
    customer_email = forms.EmailField(label="Ваш Email", max_length=255, required=True)
    robot = forms.ChoiceField(
        choices=[(serial, serial) for serial in available_serials],
        label="Выберите серийный номер робота",
    )
