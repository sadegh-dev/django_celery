from django.shortcuts import render, redirect
from .forms import SumNumbersForm
from .models import SumNumbers
from .tasks import adding

def home(request):
    numbers = SumNumbers.objects.all()
    if request.method == 'POST':
        form = SumNumbersForm(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            num = SumNumbers(q=cd['q'], w=cd['w'])
            num.save()
            result = adding.delay(cd['q'], cd['w'], num.id) 
            num.id_task = result.id
            num.save()
            return redirect('sum:home')
    else :
        form = SumNumbersForm()
    context = {
        'form':form ,
        'numbers' : numbers ,
    }
    return render(request, 'num/home.html', context)

