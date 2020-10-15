from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import ContactForm
from articles.models import Contact,Article,Author,Category,Comment,Reply

#index page view
def index_view(request):
    articles = Article.objects.all().order_by('-date')[:3]
    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            #getting values of the form field
            m_name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            #saving the contacts
            contact = Contact(name=m_name,email=email_address,message=mail_message)
            contact.save()
            return redirect('/')
    else:
        form = ContactForm()
    return render(request,'index_view.htm',{'form':form,'articles':articles})


#about page view
def about_view(request):
    return render(request, 'about_view.htm')