from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import emp
from .forms import *

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

def grievances(request):
    return HttpResponse('grievances')
def manager_info(request):
    return render(request, 'myapp/Managers.html')
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
def update_employee(request, empid):
    employee = Employee, empid=empid

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view_emp')  # Redirect to the employee list view
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'update_employee.html', {'form': form, 'employee': employee})


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