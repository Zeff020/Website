from django.shortcuts import render

# Create your views here.
def quantumdiagrams(request):
    return render(request, 'quantumdiagrams/quantumdiagramsmain.html')