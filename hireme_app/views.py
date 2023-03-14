from django.shortcuts import render
from hireme_app.models import Jobtitle

def jobtitle_list(request):
    Jobtitles=Jobtitle.objects.all()
    return render(
        request,"title_list.html",{"jobtitles":Jobtitles}
    )

def jobtitle_add(request):
    if(request.method=="POST"):
        jobtitle= request.POST['Title']
        Jobtitle.objects.create(title=jobtitle)
    return render(
        request,"title_add.html"
    )