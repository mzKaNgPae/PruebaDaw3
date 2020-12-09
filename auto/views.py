from django.shortcuts import render
from .models import Auto

# Create your views here.

def lista_autos(request):
    autos = Auto.objects.all()

    page = request.GET.get('page',1)
    paginator = Paginator(projects,3)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, "portfolio/portfolio.html",{'projects':projects})