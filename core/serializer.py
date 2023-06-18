from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import CalorieModel
import requests
from api.config import project_config
from extras.models import ExpectedCalories
from rest_framework.validators import ValidationError


class CalorieSerializer(ModelSerializer):
    user_id = ReadOnlyField()
    time = ReadOnlyField()
    date = ReadOnlyField()
    met_expectations = ReadOnlyField()

    class Meta:
        model = CalorieModel
        fields = ["user_id", "time", "date", "met_expectations", "total_calories", "text"]

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data["user_id"] = request.user
        expected = ExpectedCalories.objects.filter(user_id=request.user.id).first()
        if expected is None:
            raise ValidationError({
                "error": "Please set the expected calorie",
                "code": 400
            })
        try:
            data = validated_data["total_calories"]
        except KeyError:
            total = 0
            sum_calories = 0.0
            response = requests.post(project_config.API_URL,
                                     json={"query": f'{validated_data["text"]}',
                                           "timezone": "Asia/Kolkata"},
                                     headers={"Content-Type": "application/json",
                                              "x-app-id": project_config.APP_ID, "x-app-key": project_config.API_KEY})
            for i in response.json()["foods"]:
                total += i["nf_calories"]
            validated_data["total_calories"] = total
            entries = CalorieModel.objects.filter(user_id=request.user.id)
            for i in entries:
                sum_calories += float(i.total_calories)
            sum_calories += float(validated_data["total_calories"])
            if sum_calories <= expected.expected:
                validated_data["met_expectations"] = True
            else:
                for i in entries:
                    i.met_expectations = False
                    i.save()
        return super().create(validated_data)


class CoreResponseSerializer(ModelSerializer):
    user_id = ReadOnlyField()
    time = ReadOnlyField()
    date = ReadOnlyField()
    met_expectations = ReadOnlyField()
    total_calories = ReadOnlyField()
    text = ReadOnlyField()

    class Meta:
        model = CalorieModel
        fields = ["user_id", "time", "date", "met_expectations", "total_calories", "text"]
