from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail


def homepage(request):
    return render(request, "questionwebapp/homepage.html")


def contact(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        about = request.POST.get("about")
        description = request.POST.get("description")

        email_subject = "📩 New Contact Form Submission"
        email_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);">
                <h2 style="color: #2C3E50; text-align: center;">📩 New Contact Form Submission</h2>
                <p><strong>Name:</strong> {full_name}</p>
                <p><strong>Email:</strong> <a href="mailto:{email}" style="color: #3498db;">{email}</a></p>
                <p><strong>About:</strong> {about}</p>
                <p><strong>Description:</strong></p>
                <p style="background: #ecf0f1; padding: 10px; border-radius: 5px;">{description}</p>
                <hr style="border: none; border-top: 1px solid #ddd;">
                <p style="text-align: center; font-size: 12px; color: #7f8c8d;">This email was sent from the contact form.</p>
            </div>
        </body>
        </html>
        """

        try:
            send_mail(
                email_subject,
                "",
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
                html_message=email_body,  # Send HTML email
            )
            return JsonResponse(
                {"success": True, "message": "Email sent successfully!"}
            )
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return render(request, "questionwebapp/contact.html")


def about(request):
    return render(request, "questionwebapp/about.html")


def blog(request):
    return render(request, "questionwebapp/blog.html")


def services(request):
    return render(request, "questionwebapp/services.html")
