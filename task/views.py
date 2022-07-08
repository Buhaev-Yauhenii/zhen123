from django.shortcuts import render
from .forms import InputForm
from .models import MyModel
# Create your views here.

def form(request):
    if request.method =='POST':
        form = InputForm()
        data = {key:value for key, value in zip(range(0, len(request.POST.getlist('input_data'))),request.POST.getlist('input_data'))}
        MyModel.objects.create(collection=data)
    else: 
        form = InputForm()
    return render(request, 'form.html', {'form':form})


def view_data(request):
    data = MyModel.objects.values_list()
    return render(request, 'view_form.html', {'data':dict(data), 'len':len(dict(data).values())})
