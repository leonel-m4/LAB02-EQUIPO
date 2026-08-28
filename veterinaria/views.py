from django.shortcuts import render, redirect
from .models import citas
from .forms import CitaForm


def lista_citas(request):
    return render(request, "veterinaria/lista.html", {
        "citas": citas
    })


def crear_cita(request):

    if request.method == "POST":
        form = CitaForm(request.POST)

        if form.is_valid():

            nueva_cita = {
                "id": len(citas) + 1,
                "dueno": form.cleaned_data["dueno"],
                "mascota": form.cleaned_data["mascota"],
                "servicio": form.cleaned_data["servicio"],
                "fecha": str(form.cleaned_data["fecha"])
            }

            citas.append(nueva_cita)

            return redirect("lista_citas")

    else:
        form = CitaForm()

    return render(request, "veterinaria/formulario.html", {
        "form": form
    })