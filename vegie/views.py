from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Receipe


@login_required(login_url='login')
def receipes(request):
    
    print(request.user)
    print(request.user.is_authenticated)

    if request.method == "POST":
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )

        return redirect("receipes")

    queryset = Receipe.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(
            receipe_name__icontains=request.GET.get("search")
        )

    context = {
        "receipes": queryset
    }

    return render(request, "receipes.html", context)


@login_required(login_url='login')
def update_receipe(request, id):

    receipe = Receipe.objects.get(id=id)

    if request.method == "POST":
        receipe.receipe_name = request.POST.get("receipe_name")
        receipe.receipe_description = request.POST.get("receipe_description")

        if request.FILES.get("receipe_image"):
            receipe.receipe_image = request.FILES.get("receipe_image")

        receipe.save()

        return redirect("receipes")

    context = {
        "receipe": receipe
    }

    return render(request, "update_receipes.html", context)


@login_required(login_url='login')
def delete_receipe(request, id):

    receipe = Receipe.objects.get(id=id)
    receipe.delete()

    return redirect("receipes")