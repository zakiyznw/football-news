from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406496044',
        'name': 'Zakiy Nashrudin Wahid',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)