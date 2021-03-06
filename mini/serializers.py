from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Student, Project

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    project= serializers.HyperlinkedRelatedField(
        view_name= 'project_detail',
        many= True,
        read_only = True
    )
    student_url=serializers.ModelSerializer.serializer_url_field(view_name='student_detail')
    class Meta:
        model = Student
        fields = ('id', 'photo_url','student_url', 'nationality','name', 'quote', 'project')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.HyperlinkedRelatedField(
        view_name='student_detail', 
        read_only=True
    )

    student_id = serializers.PrimaryKeyRelatedField(
        queryset= Student.objects.all(),
        source = 'name'
    )
    class Meta:
        model = Project
        fields = ('id', 'name', 'title','preview_url', 'student_id')