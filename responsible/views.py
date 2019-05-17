from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def landingpage(request):
    return render(request, 'responsible/landingpage.html')


def main(request):
    form = PostForm()
    return render(request, 'responsible/main.html', {'form' : form})