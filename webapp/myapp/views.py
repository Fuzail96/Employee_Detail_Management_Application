from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.models import User, auth
from django.contrib import messages


def home(request):
    return render(request, "welcome.html")


def load_form(request):
    form = EmployeeForm
    return render(request, "index.html", {'form' : form} )


def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/show')


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')


def show(request):
    employee = Employee.objects.all
    return render(request, 'show.html', {'employee': employee})


def search(request):
    given_name=request.POST['name']
    employee= Employee.objects.filter(fName__icontains=given_name)
    return render(request, 'show.html', {'employee': employee})

def register(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['re_password']

            if password == password2:
                if User.objects.filter(username=name).exists():
                    messages.info(request, 'Name Already In Use')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already In Use')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=name, email=email, password=password)
                    user.save()
                    messages.info(request, "Thanks For Registering.")
                    return redirect('register')
            else:
                messages.info(request, 'Password Not Matching')
                return redirect('register')

        else:
            return render(request, 'register.html')
    except Exception as e:
        return ("Error:" + str(e) + "All Fields Are Required")
  

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("show")
        elif user is None:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

