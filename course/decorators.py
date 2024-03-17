from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import Http404
from coursemanagement.models import CourseSetting

def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, calender_url=Http404):
    """
    Decorator for views that checks that the logged-in user is a student,
    redirects to the log-in page if necessary.
    """
    # Assuming you have an actual_decorator function defined somewhere in your code
    if function:
        return actual_decorator(function)
    return actual_decorator

# Check if at least one CourseSetting record with add_drop=True exists
is_calendar_on = CourseSetting.objects.filter(add_drop=True).exists()
