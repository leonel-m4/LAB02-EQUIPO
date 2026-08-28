from django import forms


class CitaForm(forms.Form):

    dueno = forms.CharField(
        label="Nombre del dueño",
        max_length=100
    )

    mascota = forms.CharField(
        label="Nombre de la mascota",
        max_length=100
    )

    servicio = forms.CharField(
        label="Servicio",
        max_length=100
    )

    fecha = forms.DateField(
        label="Fecha de la cita",
        widget=forms.DateInput(
            attrs={"type": "date"}
        )
    )