# Create your views here.
from django.shortcuts import render,redirect
# imported our models
from django.core.paginator import Paginator

from . models import Song


# paginator used to navigate in tables
# can take id refrence also
def index(request):
    paginator= Paginator(Song.objects.all(),1)
    # can do by id also
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj":page_obj}
    # print(page_obj)
    return render(request,"App/index.html",context)
def addmusic(request):
    if request.method=="POST":
        print("df")
    else:
        return render(request,"app/addmusic.html");
