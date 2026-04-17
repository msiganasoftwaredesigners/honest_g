from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
# from .forms import FormWithCaptcha   ← remove or comment this if not using

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('your_name', '').strip()
        number = request.POST.get('your_number', '').strip()
        email = request.POST.get('your_email', '').strip()
        message = request.POST.get('message', '').strip()

        # Basic validation
        if not all([name, number, email, message]):
            messages.error(request, "All fields are required.")
            return render(request, 'contact-us.html')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            number=number,
            email=email,
            message=message
        )

        # Email to admin
        subject = f'New Contact Message from {name}'
        email_message = f"Name: {name}\nNumber: {number}\nEmail: {email}\nMessage: {message}"

        try:
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            # Confirmation email to user
            user_subject = 'Thank You for Contacting Honest Gt'
            user_message = (
                f"Hello {name},\n\n"
                "Thank you for reaching out to us. We have received your message and will get back to you within 24 hours.\n\n"
                "Best regards,\n"
                "The Honest Gt Team"
            )
            send_mail(
                user_subject,
                user_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
        
        except Exception as e:
            messages.error(request, "Your message was saved, but we couldn't send the email notification right now.")

        return redirect('contact-us')

    return render(request, 'contact-us.html')