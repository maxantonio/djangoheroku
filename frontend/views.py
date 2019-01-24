from django.shortcuts import render

# Create your views here.

# Create your views here.
def index(request):


    context = {
        'meta_description': "Base del meta"}
    return render(request, 'frontend/index.html', context)
