from django.shortcuts import render, get_object_or_404
from .models import Authors_Guide, EditorialMembers,AboutHeaders,AboutPage, ContactUs,BookDetailPost
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls  import reverse
from .utils import latest_uploads

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

def editorial_board(request):
    editorial_members= EditorialMembers.objects.all()
    context = {
        "editorial_members":editorial_members
    }
    return render(request, "editorial-board.html", context)


def journal_detail(request):
    context = {}
    return render(request, "journal-detail.html", context) 


#The Contact form
def contact_message(request):
    if request.method == "GET":
        # return HttpResponse("this method is not allowed")
        return HttpResponseRedirect('/about')
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
        try:
            new_message=ContactUs(name=name, email=email, subject=subject, messagename=message)
            new_message.save()
            messages.success(request, "Message sent successfully")
            return HttpResponseRedirect(reverse("about"))
        except:
            messages.error(request, "Failed to send Message")
            return HttpResponseRedirect(reverse("about"))
        

 #The Authors Guide Button  
def authors_guide_download(request) :
        document = get_object_or_404(Authors_Guide)
        try:
            response = HttpResponse(document.author, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{document.author.name}"'
            return response
        except ValueError:
            messages.info(request, 'Document not found')
            return HttpResponseRedirect(reverse("home"))
        
#The Journal download Button  
def download(request, pk) :
        document = get_object_or_404(BookDetailPost, pk=pk)
        try:
            response = HttpResponse(document.book, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{document.book.name}"'
            return response
        except ValueError:
            messages.info(request, 'Document not found')
            return HttpResponseRedirect(reverse("home"))
        