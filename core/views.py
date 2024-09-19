from django.shortcuts import render

def landingPage (request):
    return render(request, ('landing_page\landing_page.html'))