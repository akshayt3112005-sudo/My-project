from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
 

# Create your views here.
def index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'About.html')

def service(request):
    return render(request,'service.html')

def navbar(request):
    return render(request,'navbar.html')

def traffic(request):
    return render(request,'traffic.html')

def contaner(request):
    return render(request,'contaner.html')
 
def contaner2(request):
    return render(request,'contaner2.html')

#def contact(request):
    #return render(request,'contact.html')q

def footer(request):
    return render(request, 'footer.html')





def contact(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        address = request.POST.get("address")

        message = f"""
New Contact Form Message

Name: {full_name}
Email: {email}
Phone: {phone}
Subject: {subject}
Address / Project Location: {address}
"""

        send_mail(
            subject=f"Contact Form: {subject}",
            message=message,
            from_email="parassapkale398@gmail.com",
            recipient_list=["parassapkale398@gmail.com"],
            fail_silently=False,
        )

        return render(request, "contact.html", {
            "success": "Your message has been sent successfully!"
        })

    return render(request, "contact.html")