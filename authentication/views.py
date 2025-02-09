from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator  

UserProfile = get_user_model()

# Create your views here.



def register(request):
    if request.method == "POST":
        First_name = request.POST.get("First_name")
        Last_name = request.POST.get("Last_name")
        email = request.POST.get("email")
        create_password = request.POST.get("create_password")
        confirm_password = request.POST.get("confirm_password")

        print("🟢 Registration Form Submitted")  

        if create_password != confirm_password:
            print("❌ Passwords do not match!")  # Debugging print
            messages.error(request, "Passwords do not match!")
            return render(request, "authentication/sign_up.html")

        if UserProfile.objects.filter(email=email).exists():
            print("❌ Email already exists!")  # Debugging print
            messages.error(request, "Email already in use!")
            return render(request, "authentication/sign_up.html")

        print("✅ Creating user now...")
        user = UserProfile.objects.create_user(
            username=email.split("@")[0],
            first_name=First_name,
            last_name=Last_name,
            email=email,
            password=create_password,
            is_active=False,
        )

        print("✅ User created successfully!")

        # Generate email verification token
        current_site = get_current_site(request)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        verification_link = f"http://{current_site.domain}{reverse('authentication:activate', kwargs={'uidb64': uid, 'token': token})}"

        print(f"🔗 Generated verification link: {verification_link}")

        subject = "Verify your email"
        message = f"Hi {user.first_name},\n\nClick the link below to activate your account:\n{verification_link}"

        try:
            sent = send_mail(subject, message, "your-email@gmail.com", [user.email], fail_silently=False)
            print(f"📩 Email sent: {sent}")  
        except Exception as e:
            print(f"❌ Email failed: {e}")  

        messages.success(request, "Account created! Check your email for verification.")
        return redirect("login")

    print("🔴 Registration Page Loaded (GET request)")  
    return render(request, "authentication/sign_up.html")



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserProfile.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Email verified! You can now log in.")
        return redirect("login")
    else:
        messages.error(request, "Invalid or expired activation link!")
        return redirect("register")

def send_verification_email(user, request, uid, token):
    current_site = get_current_site(request)
    subject = "Activate Your Account"
    verification_link = f"http://{current_site.domain}{reverse('activate', kwargs={'uidb64': uid, 'token': token})}"
    
    message = f"Hi {user.first_name},\n\nClick the link below to activate your account:\n{verification_link}"

    send_mail(
        subject,
        message,
        'debbienjenga@@gmail.com',  # Change this to match EMAIL_HOST_USER
        [user.email],
        fail_silently=False,
    )
    print("Email sent successfully!")  # Debugging print

def login_view(request):
    return render(request, "authentication/login.html")