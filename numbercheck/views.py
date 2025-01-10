from django.shortcuts import render

def check_number_view(request):
    result = None

    if request.method == "POST":
        number = request.POST.get("number")
        try:
            number = int(number)
            result = "Even" if number % 2 == 0 else "Odd"
        except ValueError:
            result = "Invalid input. Please enter a number."

    return render(request, "numbercheck.html", {"result": result})
