from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']



        contact = Contact(name=name,email=email,phone=phone,message=message)

        contact.save()

        send_mail(
                'Enquiry',
                'There has been a Enquiry: ' + message ,
                'djangoemail321@gmail.com',
                ['knowledgeislightconsult@gmail.com', 'j.pollyn@gmail.com', 'kintade@yahoo.com'],
                fail_silently=False


        )

        messages.success(request, 'We have recieved your information, one of our staff will contact you soon')

    return render(request, 'contact/contact.html')


        

