from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.
def home(request):
    print("inside the home")
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        print("form is in post ")
        if form.is_valid():
            print("form is valid")
            form.save()
    form= ImageForm()
    img=Image.objects.all()
    return render(request,'myapp/home.html',{'img':img, 'form':form})