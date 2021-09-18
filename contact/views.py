from django.shortcuts import render,redirect
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm
# Create your views here.
def send_email(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         subject = form.cleaned_data['subject']
         #phone = form.cleaned_data['phone']
         form_email = form.cleaned_data['form_email']
         message = form.cleaned_data['message']

         try:
            send_mail(subject,message,form_email,['admin@example.com'])
         except BadHeaderError:
            return HttpResponse('invalid header')

         return redirect('contact:send_success')

   else:
      form = ContactForm()

   return render(request,'contact/contact.html',{
      'form':form,
   })

def send_success(request):
   pass