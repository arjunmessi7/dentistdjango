from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def service(request):
    return render(request, 'services.html',{})

def contact(request):
    if request.method == "POST" :
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']

        send_mail(
        name,
        email,
        message,
        ['arjunmessi090@gmail.com']
        )
    
    
        return render(request, 'contact.html', {'name'})

    else:
    
        return render(request, 'contact.html',{})