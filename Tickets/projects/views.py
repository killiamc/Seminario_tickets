from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, AbonadoForm
from django.contrib.auth import authenticate, login, logout
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from projects.models import Turno
#from projects.models import 
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_data(request):
    turno = request.POST.get('turno')
    fecha = request.POST.get('fecha')
    entidad = request.POST.get('entidad')
    print(turno, fecha, entidad)
    Turno.objects.create(fecha=fecha, Persona=request.user.cedula, id=turno, estado=True, entidad=entidad)
    return JsonResponse({})


@login_required(login_url='login')
def Index(request):
    turno = request.POST.get('turno')
    print(turno)
    return render(request, 'index.html')

def Login(request):

    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, "Login.html", {})


def Registro(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()

            return redirect('login')
    else:
        print(form.errors)

    context = {'form': form}

    return render(request, 'Registro.html', context = context)


@login_required(login_url='login')
def Ver(request):
    Required_table = Turno.objects.all()
    print(request.user.cedula)
    Tables = Required_table.filter(Persona=request.user.cedula)
    if not Tables:
        # Tables is empty
        # Add your code here to handle the empty case
        context = {'table': 'No hay turnos asignados'}


    else:
        # Tables is not empty
        # Add your code here to handle the non-empty case
        print(Tables)
        Data = pd.DataFrame(list(Tables.values()))
        print(Data.fecha)
        fig = go.Figure(data=[go.Table(
            header=dict(values=['Fecha', 'Entidad', 'Turno']),
            cells=dict(values=[Data.fecha, Data.entidad, Data.id],
                        align='center',
                        fill_color = 'lightgrey',
                        alignsrc = 'center',
                        )),
            ])
        fig.update_layout(width=800, height=400)
        table = fig.to_html()
        context = {'table': table}



    return render(request, 'ver.html', context = context)  

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión')
    return redirect('login')