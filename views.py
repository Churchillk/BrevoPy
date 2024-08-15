from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def send_email(author, taskname, taskdate, email):
    subject = f"Task Claimed Reminder:'"
    message = f"Dear {author},\n\nPlease complete the task '{taskname}' by {taskdate}. Timeliness is appreciated.\n\nThank you."
    sender_email = 'EMAIL_HOST_USER_FROM_BREVO'
    recipient_email = f'{email}'
    context = {
        'author': author,
        'taskname': taskname,
        'taskdate': taskdate,
    }
    message = render_to_string('Home/email.html', context)

    # Create the email
    email = EmailMessage(
        subject,
        message,
        sender_email,  # Sender email address (must match your Brevo account email)
        [recipient_email]
    )
    email.content_subtype = 'html'
    
    email.send()
