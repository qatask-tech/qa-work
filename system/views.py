from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime

# Correct imports
from service.models import Service  # Import Service from service app
from system.forms import usersForm, ContactForm
from system.utils import is_even_or_odd
from news.models import News



# Global data dictionary
data = {
    'value': 2,
    'f': [10, 20, 30, 40],
    's': [10, 20, 30, 40],
    'v': "Welcome to Tech Comp",
}



# Home page view
def home(request):
    news_list = News.objects.all()  # Fetch news items
    services = Service.objects.all()  # Fetch service items
    context = {
        'news_list': news_list,
        'services': services,
        'current_year': datetime.now().year
    }
    return render(request, 'home.html', context)




# News detail view
def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'news_detail.html', {'news_item': news_item})



# About Us page view
def aboutus(request):
    output = None
    if request.method == "POST":
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        try:
            result = int(num1) + int(num2)
            output = f"The sum of {num1} and {num2} is {result}."
        except (ValueError, TypeError):
            output = "Invalid input. Please enter valid numbers."
    return render(request, 'aboutus.html', {'output': output})

# Contact page view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Services page view
def services(request):
    services = Service.objects.all()
    search_term = request.GET.get('servicename', '')
    if search_term:
        services = services.filter(service_title__icontains=search_term)
    paginator = Paginator(services, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'services.html', {
        'page_obj': page_obj,
        'search_term': search_term,
        'lastpage': paginator.num_pages,
        'totalPagelist': list(paginator.page_range),
    })
    
def course(request):

    return render(request, 'course.html')

# Calculator view
def calculator(request):
    result = None
    if request.method == "POST":
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operation = request.POST.get('operation')
        try:
            num1 = float(num1)
            num2 = float(num2)
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero."
        except ValueError:
            result = "Invalid input. Please enter numbers."
    return render(request, 'calculator.html', {'result': result})

# User form view
def UsersFormView(request):
    message = None
    if request.method == "POST":
        form = usersForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            message = f"Form submitted successfully! Username: {username}, Email: {email}"
        else:
            message = "Form submission failed. Please correct the errors."
    else:
        form = usersForm()
    return render(request, 'userform.html', {'form': form, 'message': message})

# Number check view
def check_number_view(request):
    result = None
    if request.method == "POST":
        if not request.POST.get('number'):
            return render(request, "numbercheck.html", {"error": True})
        number = request.POST.get("number")
        result = is_even_or_odd(number)
    return render(request, "numbercheck.html", {"result": result})

# Marksheet view
def marksheet_view(request):
    result = None
    if request.method == "POST":
        try:
            student_name = request.POST.get("student_name", "Unknown Student")
            subject1 = int(request.POST.get("subject1", 0))
            subject2 = int(request.POST.get("subject2", 0))
            subject3 = int(request.POST.get("subject3", 0))
            total = subject1 + subject2 + subject3
            percentage = total / 3
            grade = "A" if percentage >= 75 else ("B" if percentage >= 50 else "C")
            result = {
                "student_name": student_name,
                "total": total,
                "percentage": percentage,
                "grade": grade,
            }
        except ValueError:
            result = {"error": "Invalid marks entered. Please enter numeric values."}
    return render(request, "marksheet.html", {"result": result})

# Manual form view
# system/views.py
def manual_form_view(request):
    errors = []
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        age = request.POST.get('age', '').strip()

        # Validate name
        if not name:
            errors.append("Name is required.")
        elif len(name) < 3:
            errors.append("Name must be at least 3 characters long.")

        # Validate email
        if not email:
            errors.append("Email is required.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("Invalid email format.")

        # Validate age
        if not age:
            errors.append("Age is required.")
        else:
            try:
                age = int(age)
                if age < 18:
                    errors.append("You must be at least 18 years old.")
            except ValueError:
                errors.append("Age must be a valid number.")

        # If no errors, display success message
        if not errors:
            return render(request, 'manual_form.html', {
                'success': True,
                'name': name,
                'email': email,
                'age': age,
            })

    # Render the form with errors (if any)
    return render(request, 'manual_form.html', {'errors': errors})

