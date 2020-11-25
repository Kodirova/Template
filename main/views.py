from django.shortcuts import render

# Create your views he
def index(request):
    return render(request, 'index.html')
