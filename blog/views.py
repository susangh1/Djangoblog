from django.shortcuts import render,HttpResponse
from datetime import datetime
from blog.models import Contact


# Create your views here.
def index(request):
   
    return render(request,'index.html')
    #return HttpResponse("This is homepage")
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        email = request.POST.get('email')
        Phone = request.POST.get('Phone')
        Description = request.POST.get('Description')
        contact =Contact( Name = Name, email = email, Phone = Phone ,Description = Description, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')
    


