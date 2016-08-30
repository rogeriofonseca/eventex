from django.shortcuts import render

# Create your views here.
def home(request):
    return 'index'
    #return render(request, 'index.html')