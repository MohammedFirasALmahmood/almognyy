from rest_framework import serializers

from firstyear.models import WGrammar
from manager.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class WGrammarSerializer(serializers.ModelSerializer):
    class Meta:
        model = WGrammar
        fields = "__all__"
