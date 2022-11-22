from django.shortcuts import render, redirect
from . models import Calculator

# Create your views here.
def home(request):
    show_data = Calculator.objects.all()
    return render(request, 'calculator/home.html', {'shows':show_data})

def calculation(request):
    
    # Grab the data from HTML Form and store  on variable
        number_1 = request.POST['number1']
        number_2 = request.POST['number2']

        if 'add' in request.POST:
            result = round(float(number_1) + float(number_2),2)
            sym = '+'
        
        elif 'sub' in request.POST:
            result = round(float(number_1) - float(number_2),2)
            sym = '-'

        elif 'mul' in request.POST:
            result = round(float(number_1) * float(number_2),2) 
            sym = 'X'

        elif 'div' in request.POST:
            result = round(float(number_1) / float(number_2), 2)
            sym = '/'

    # Now store data into database with some calculation
        store_data = Calculator.objects.create(num_1=number_1, num_2 = number_2, sym=sym, result = result)
        return redirect('home')

def delete_data(request, pk):
    del_data = Calculator.objects.get(id=pk)
    del_data.delete()
    return redirect('home')