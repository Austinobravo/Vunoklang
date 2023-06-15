from django.shortcuts import render, get_object_or_404
from .models import Authors_Guide, EditorialMembers,AboutImages,AboutPage, ContactUs,BookDetailPost
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls  import reverse
from .utils import latest_uploads

# Create your views here.

def home(request):
    journals=BookDetailPost.objects.all().order_by("-created_on")[:5]
    last_journal=BookDetailPost.objects.last()
    date_str=str(last_journal.created_on)
    date_str.split(" ")
    name="name"
    date_split=date_str.split(" ")[0].split("-")
    day, month, year=date_split[2], date_split[1], date_split[0]
  
    context = {"journals":journals, "last_journal":last_journal, "day":day, "month":month, "year":year, "name":name}
    return render(request, 'index.html', context)

def all_journals(request):
    journals=BookDetailPost.objects.all()
    name="name"
    context={"journals":journals, "name":name}
    return render(request, "all_journals.html", context)




def about_page(request):
    contents=AboutPage.objects.all()
    pictures=AboutImages.objects.all()
    print(contents)
    context = {"contents":contents, "pictures":pictures}
    return render(request, "about_page.html", context)

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
            return HttpResponseRedirect(reverse("about_page"))
        except:
            messages.error(request, "Failed to send Message")
            return HttpResponseRedirect(reverse("about_page"))
        

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
        