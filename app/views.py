from django.shortcuts import render


# views for all the three templates for url mapping # 
def register(request):
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')
