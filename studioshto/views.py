from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import ContactForm
from articles.models import Contact,Article,Author,Category,Comment,Reply
from utilities.models import Welcome, About, Solution
from services.models import Project, Service

#index page view
def index_view(request):

    # @db queries
    articles = Article.objects.all().order_by('-date')[:3]
    services = Service.objects.all()
    solutions = Solution.objects.all()
    welcomes = Welcome.objects.all()

    # @contact form validation
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

    # @rendering view,
    return render(request,'index_view.htm',{'form':form,'articles':articles,'services':services,'solutions':solutions,'welcomes':welcomes})


#about page view
def about_view(request):

    # @db queries
    abouts = About.objects.all()

    # @rendering view
    return render(request, 'about_view.htm',{'abouts':abouts})