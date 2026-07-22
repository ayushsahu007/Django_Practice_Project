from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Receipe
from django.contrib import messages


@login_required(login_url='login')
def receipes(request):

    # Admin cannot create recipes
    if request.user.is_staff and request.method == "POST":
        messages.error(request, "Admin cannot create recipes.")
        return redirect("receipes")

 # Normal user can create
    if request.method == "POST":
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")
        
        print(request.user)
        print(request.user.is_authenticated)
        print(request.user.id)
       
        receipe =  Receipe.objects.create(
            user=request.user,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        
        print(receipe.user)
        print(receipe.user_id)

        receipe.save()

        return redirect("receipes")
    
    
    if request.user.is_staff:
        queryset = Receipe.objects.all().order_by("user__username", "id")
    else:
       queryset = Receipe.objects.filter(user=request.user)

    search = request.GET.get("search")
    if search:
        queryset = queryset.filter(
            receipe_name__icontains=search
        )

    context = {
        "receipes": queryset
    }

    return render(request, "receipes.html", context)


@login_required(login_url='login')
def update_receipe(request, id):

    if request.user.is_staff:
        receipe = get_object_or_404(Receipe, id=id)
    else: 
       receipe = get_object_or_404(
        Receipe,
        id=id,
        user=request.user
    )

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

    if request.user.is_staff:
        receipe = get_object_or_404(
            Receipe,
            id=id
        )
    else:
        receipe = get_object_or_404(
            Receipe,
            id=id,
            user=request.user
        )

    receipe.delete()

    return redirect("receipes")