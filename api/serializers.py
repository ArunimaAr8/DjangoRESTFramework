from rest_framework import serializers

class poststudentdetailsSerializer(serializers.Serializer):
    student_id = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=50)
    mobile = serializers.IntegerField()