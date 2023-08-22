from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_emp(request):
    return render(request, 'add_emp.html')
def add_action(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        profile_image = request.POST['profile_image']
        dob = request.POST['dob']
        address = request.POST['address']
        cv = request.POST['cv']

        add_emp_data = Employee.objects.create(name=name, email=email, password=password, mobile=mobile, salary=salary, bonus=bonus, profile_image=profile_image, dob=dob, address=address, cv=cv)

        emp_data = Employee.objects.all()
        dict = {
            'emp_data': emp_data
        }
        return render(request, 'view_all_emp.html', dict)
        
def view_all_emp(request):
        emp_data = Employee.objects.all()
        dict = {
            'emp_data': emp_data
        }
        return render(request, 'view_all_emp.html', dict)

def update_emp(request, id):
    emp_data = Employee.objects.get(id=id)
    dict = {
        'emp_data': emp_data
    }
    return render(request, 'update_emp.html', dict)
def update_action(request, id):
     if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        profile_image = request.POST['profile_image']
        dob = request.POST['dob']
        address = request.POST['address']
        cv = request.POST['cv']

        add_emp_data = Employee.objects.get(id=id)

        add_emp_data.name = name
        add_emp_data.email = email
        add_emp_data.password = password
        add_emp_data.mobile = mobile
        add_emp_data.salary = salary
        add_emp_data.bonus = bonus
        add_emp_data.profile_image = profile_image
        add_emp_data.dob = dob
        add_emp_data.address = address
        add_emp_data.cv = cv
        add_emp_data.save()

        emp_data = Employee.objects.all()
        dict = {
            'emp_data': emp_data
        }
        return render(request, 'view_all_emp.html', dict)
     
def delete_emp(request, id):
     if request.method == 'POST':
        add_emp_data = Employee.objects.get(id=id)
        add_emp_data.delete()

        emp_data = Employee.objects.all()
        dict = {
            'emp_data': emp_data
        }
        return render(request, 'view_all_emp.html', dict)