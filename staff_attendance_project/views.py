# api/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Staff, CheckInOut

@api_view(['POST'])
def staff_login(request):
    # Implement staff authentication logic here
    # You can use request.data to access POST data

@api_view(['POST'])
def staff_checkin(request):
    # Implement check-in logic here
    # You can use request.data to access POST data

@api_view(['POST'])
def staff_checkout(request):
    # Implement check-out logic here
    # You can use request.data to access POST data

@api_view(['GET'])
def view_attendance(request):
    # Implement logic to retrieve attendance records
    # You can use CheckInOut.objects.filter() to filter records

