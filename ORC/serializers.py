from rest_framework import serializers
from .models import *

class WorkorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workorder
        fields = ('resident_name', 'workorder_id', 'workorder_Description',
                  'workorder_category', 'workorder_priority', 'property_number',
                  'workorder_opendate', 'workorder_duedate', 'workorder_closedate',
                  'is_open')


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ('resident_id', 'user', 'resident_name', 'resident_occupation',
                  'resident_emailaddress', 'resident_marital_status',
                  'resident_familymember_count', 'resident_petdetails', 'resident_contactdetails',
                  'resident_startdate', 'resident_enddate')