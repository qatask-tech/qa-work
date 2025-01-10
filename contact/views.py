from django.shortcuts import render
from contact.forms import ContactForm  # Ensure this is the correct path

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging
            form.save()  # Save the form data to the database
            print("Data saved")  # Debugging
            return render(request, 'contact/contact.html', {'form': ContactForm(), 'success': True})
        else:
            print("Form is not valid:", form.errors)  # Debugging
            return render(request, 'contact/contact.html', {'form': form, 'success': False})
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
