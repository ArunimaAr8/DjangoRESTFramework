from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import *
from .serializers import *


class getstudentlist(APIView):
    def get(self, request):
        result = list(student.objects.filter().values())
        return JsonResponse(result, status=status.HTTP_200_OK, safe=False)


class getspecificstudentslist(APIView):
    def get(self, request, stu_id):
        result = list(student.objects.filter(student_id=stu_id).values())
        return JsonResponse(result, status=status.HTTP_200_OK, safe=False)


class poststudentdetails(APIView):
    def post(self, request):
        serializer = poststudentdetailsSerializer(data=request.data)
        if serializer.is_valid():
            student_id1 = serializer.data["student_id"]
            name = serializer.data["name"]
            mobile = serializer.data["mobile"]
            # create entry in table
            student.objects.create(
                student_id=student_id1,
                name=name,
                mobile=mobile)
            message = {"Message": "Student Entry Created Successfully"}
            return JsonResponse(message, status=status.HTTP_201_CREATED, safe=False)
