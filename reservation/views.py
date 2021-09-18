from django.shortcuts import render
from .forms import ReserveTableForm
# Create your views here.
def reserve_table(request):
   reserve_form = ReserveTableForm()
   if request.method == 'POST':
      reserve_form = ReserveTableForm(request.POST)
      if reserve_form.is_valid():
         reserve_form.save()


   return render(request,'reservation/reservation.html',{
      'form':reserve_form,
   })