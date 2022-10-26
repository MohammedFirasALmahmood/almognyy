from rest_framework import serializers

from firstyear.models import AGrammar4M
from firstyear.models import AGrammer1
from firstyear.models import AGrammer4
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


class AGrammar1Serializer(serializers.ModelSerializer):
    class Meta:
        model = AGrammer1
        fields = "__all__"


class AGrammar4MSerializer(serializers.ModelSerializer):
    class Meta:
        model = AGrammar4M
        fields = "__all__"


class AGrammar4Serializer(serializers.ModelSerializer):
    class Meta:
        model = AGrammer4
        fields = "__all__"
