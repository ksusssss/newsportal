from django.shortcuts import render
from .forms import SupplyNewsForm
from django.contrib import messages

# Create your views here.

# def main_page(request):
#     return render(request, 'main.html')

def supply_news(request):
    error = ''
    if request.method == 'POST':
        form = SupplyNewsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Ошибка'


    form = SupplyNewsForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'supply-forms.html', data)
