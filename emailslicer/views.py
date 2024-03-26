from django.shortcuts import render

def email_slicer(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        if '@' in email:
            username, domain = email.split('@')
            custom_message = f"Hello {username}, welcome to {domain}!"
            return render(request, 'slicedemail.html', {'username': username, 'domain': domain, 'custom_message': custom_message})
        else:
            error_message = "Invalid email address. Please try again."
            return render(request, 'slicedemail.html', {'error_message': error_message})
    return render(request, 'slicedemail.html')
