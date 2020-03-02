from django.shortcuts import render

# Create your views here.
def index(request):
    """The homepage for Pizza."""
    return render(request, 'pizza/index.html')