from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import emp
from .models import manager
from .forms import *
from django.urls import reverse

# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Invalid username or password"))
            return redirect('loginuser')

    else:
        return render(request, 'myapp/login.html')
def home(request):
    return render(request, 'myapp/Home.html')
def add_emp(request):
    
    form = EmployeeForm()
    if request.method == 'POST':
            form = EmployeeForm(request.POST, request.FILES)
            if form.is_valid():
                employee = form.save()
                return redirect('home')   
    context = {
            'form': form,
        }

    return render(request, 'myapp/ADd.html',context)
def view_emp(request):
    employees = emp.objects.all()
    return render(request, 'myapp/viewemp.html', {'employees': employees})
<<<<<<< HEAD
=======

def grievances(request):
    return HttpResponse('grievances')



>>>>>>> 4bc089a1d1c5f2e08827ca480af6f1b153e3cd5e
def manager_info(request):
    manager1=manager.objects.all()
    return render(request, 'myapp/managert.html', {'manager1':manager1})




def department(request):
    form = DepartmentForm(request.POST or None)
    employees = emp.objects.all()

    if request.method == "POST":
        if form.is_valid():
            selected_department = form.cleaned_data.get("department")
            if selected_department != 'select':
                employees = emp.objects.filter(department=selected_department)
        else:
            print("hi")
            

    return render(request, 'myapp/departm.html', {'form': form, 'employees': employees})
<<<<<<< HEAD
def update_employee(request, pk):
    employee = get_object_or_404(emp, pk=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view_emp')  
    context = {'form':form}
    return render(request, 'myapp/update.html', context)
=======
def update_emp(request,emp_id):
    Emp=emp.objects.get(pk=emp_id)
    print("Yes Bhai")
    return render(request,'myapp/update.html',{
        'Emp':Emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("empname")
        emp_id_temp=request.POST.get("empid")
        emp_phone=request.POST.get("phno")
        emp_address=request.POST.get("address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("deparment")
        emp_date=request.POST.get("d")

        e=emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect("/emp/home/")
>>>>>>> 4bc089a1d1c5f2e08827ca480af6f1b153e3cd5e


def delete_employee(request, emp_id):
    if request.method == 'POST':
        # Extract the employee ID from the form submission
        # You can use the emp_id parameter directly in your case
        employee_id_to_delete = emp_id

        # Get the employee by ID
        try:
            employee = emp.objects.get(pk=employee_id_to_delete)
        except emp.DoesNotExist:
            return HttpResponse("Employee not found.", status=404)

        # Delete the employee
        employee.delete()

        # Redirect to the employee list page or any other desired page
        return redirect('view_emp')

    # Handle other cases, e.g., GET requests
    return HttpResponse("Invalid request method.", status=400)


