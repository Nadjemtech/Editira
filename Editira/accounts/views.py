from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Client, Staff, Offer, notification
from .forms import ClientForm , CreateUserForm
# Create your views here.


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request,'accounts/login.html')

@login_required
def Logout(request):
	logout(request)
	return redirect('/Account/Login')


@login_required
def clientProfile(request , pk ):
    client = Client.objects.get(id=pk)
    notifs = notification.objects.filter(client=client)
    Name = client.user.username
    email = client.user.email
    FirstName = client.user.first_name
    LastName = client.user.last_name
    phone = client.phone
    address = client.address
    CCP = client.CCP
    offer = client.offer
    context = {'name': Name,
                'email': email,
               'FirstName': FirstName,
               'LastName': LastName,
               'phone': phone,
               'address': address,
               'ccp': CCP,
               'offer': offer,
               'Notifactions':notifs}
    return render(request, 'accounts/cProfile.html', context)


def RegisterView(request):
    formUser = CreateUserForm()
    form = ClientForm()
    if request.method=="POST":
        formUser = CreateUserForm(request.POST)
        form = ClientForm(request.POST)
        if form.is_valid() and formUser.is_valid() :
            user = formUser.save()
            S = form.save(commit=False)
            S.user = user
            S.save()
            messages.success(request,'your Profile Created')
            return redirect('accounts:Login')
    context = {'form':form , 'formUser':formUser }
    return render(request,'accounts/register.html',context)


def CheckNote(request,nt):
    note =notification.objects.get(id = nt)
    client = note.client.id
    if note.checked:
        return redirect(f'/Account/Client/{client}')
    else:
        note.checked = True
        note.save()
        return redirect(f'/Account/Client/{client}')