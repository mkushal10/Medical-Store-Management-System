#importing serializers
from rest_framework import serializers
from Medical.models import Company, CompanyBank


class CompanySerliazer(serializers.ModelSerializer):
    class Meta:
        model = Company
        #fields = ["name","license_no","address","contact_no"]
        fields = "__all__"

class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerliazer(instance.company_id).data
        return response