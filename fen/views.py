from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemFormSet, ItemFormSetHelper, ItemForm
from crispy_forms.layout import Submit, Button
from .models import Receipt, Item


# Create your views here.

# def index(request):
#     formset = ItemFormSet()
#     helper = ItemFormSetHelper()
#     helper.add_input(Button("add_another", "Add another", css_class="btn btn-primary"))
#     helper.add_input(Submit("submit", "Submit", css_class="btn btn-success"))
#     return render(request, "fen/index.html", {'formset': formset, 'helper': helper})


# def create_item_form(request):
#     form = ItemForm()
#     context = {
#         "form": form
#     }
#     return render(request, "fen/item_form.html", context)


def index(request):
    context = {'form': ItemForm(), 'items': Item.objects.all()}
    return render(request, "fen/create_item.html", context)


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST or None)
        if form.is_valid():
            item = form.save()
            context = {'item': item}
            return render(request, 'partials/item.html', context)

    return render(request, 'partials/item_form.html', {'form': ItemForm()})
