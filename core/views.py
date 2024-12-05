from django.shortcuts import render, HttpResponse
from api.models.models import PageVisit
def Base(request):
    queryset = PageVisit.objects.all()
    html_ = 'base.html'
    context = {
        "pageTitle": "Base"
    }
    path = request.path
    PageVisit.objects.create()
    print(queryset)
    return render(request, html_, context)