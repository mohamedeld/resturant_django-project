from django.shortcuts import render,get_object_or_404
from .models import Meals,Category
# Create your views here.
def meal_list(request):
   meal_list = Meals.objects.all()
   categories = Category.objects.all()
   return render(request,'meals/meal_list.html',{
      'meal_list':meal_list,
      'categories':categories,
   })

def meal_detail(request,slug):
   meal_detail = get_object_or_404(Meals,slug=slug)
   return render(request,'meals/meal_detail.html',{
      'meal_detail':meal_detail,
   })