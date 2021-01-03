
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import *
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import FormView
from random import shuffle

class IndexView(ListView):
    template_name = "index.html"
    queryset = Pixxx.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['random_img'] = Pixxx.objects.order_by('?').first()
        return context


class Gall(TemplateView):
    template_name ='gallery.html'

class Blog(TemplateView):
    template_name = 'blog.html'

#def contact(request):
#    form = CForm
#    return render(request,'contact.html',{'form':form})

class Single(TemplateView):
    template_name = 'single.html'

class Works(TemplateView):
    template_name = 'works.html'

class Contact(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self,form):
       subject = form.cleaned_data['subject']
       email = form.cleaned_data['email']
       message = form.cleaned_data['message']

       msg = str(email)+"     :-----"+str(message)

       try:
           send_mail(subject,msg,email,['bobzz2009@gmail.com'],fail_silently=False,)
       except BadHeaderError:
           return HttpResponse('Invalid header found.')

       return super().form_valid(form)



#def contact(request):
#    if request.method == 'GET':
#        form = ContactForm()
#    else:
#
#        form = ContactForm(request.POST)
#        if form.is_valid():
#            
#            subject = form.cleaned_data['subject']
#            from_email = form.cleaned_data['from_email']
#            message = form.cleaned_data['message']
#
#            try:
#                send_mail(subject, message, from_email, ['bobzz2009@gmail.com'],fail_silently=False,)
#            except BadHeaderError:
#                return HttpResponse('Invalid header found.')
#    return render(request,'contact.html',{'form':form})


