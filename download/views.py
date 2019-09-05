from django.shortcuts import render

# Create your views here.
def home(request):
    """ view the home page """
    return render(request, "download/index.html")
