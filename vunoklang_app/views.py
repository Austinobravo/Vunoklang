from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'index.html', context)

def event_details(request):
    context = {}
    return render(request, "event-detail.html", context)


def event_listing(request):
    context = {}
    return render(request, "event-listing.html", context)


def about_page(request):
    context = {}
    return render(request, "about_page.html", context)