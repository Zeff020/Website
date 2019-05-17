from django.shortcuts import render

# Create your views here.
def responsible(request):
    return render(request, 'responsible/main.html')