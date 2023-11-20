from django import forms
from django.forms.models import formset_factory, inlineformset_factory
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, Submit
from crispy_forms.bootstrap import PrependedText
from .models import Item, Receipt


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ('restaurant_name', 'total_people')


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'name',
            'price',
            'num_split'
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_split': forms.NumberInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Item Name',
            'price': 'Item Cost',
            'num_split': 'Split'
        }


# ItemFormSet = formset_factory(ItemForm, extra=3)


ItemFormSet = inlineformset_factory(
    Receipt,
    Item,
    form=ItemForm,
    min_num=2,
    extra=1,
    can_delete=False,
)


class ItemFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_class = 'form-horizontal'
        self.label_class = 'col-auto'
        self.field_class = 'col'
        # self.label_class = 'visually-hidden'
        # self.field_template = 'bootstrap5/layout/inline_field.html'
        self.layout = Layout(
            Div(
                Div('item_name', css_class="col"),
                Div(PrependedText('item_cost', '$'), css_class="col-3"),
                Div('num_split', css_class="col-2"),
                Div(Submit('delete', 'Delete', css_class="btn btn-danger w-100"), css_class="col-1"),
                css_class="row px-3 w-90"
            )
        )
        self.render_required_fields = True
