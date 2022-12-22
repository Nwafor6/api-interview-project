from rest_framework import serializers
from .models import (Military,
Prospect,
Areas_Of_Interest,
CallCenter,
Search,
Other_Info,
SearchConnected,)

class MilitarySerializer(serializers.ModelSerializer):
	class Meta:
		model=Military
		fields=['military_status','military_affiliation','relationship']

class ProspectSerializer(serializers.ModelSerializer):
	military=MilitarySerializer(many=False)
	class Meta:
		model=Prospect
		fields="__all__"
		

class Areas_Of_Interrest_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Areas_Of_Interest
		fields=['title']
		# fields= "__all__"
		

class CallCenterSerializer(serializers.ModelSerializer):
	class Meta:
		model=CallCenter
		fields=['PublisherBrandName','callid','sessionid','cc_inbound_transfer_company','cc_inbound_transfer_dba','cc_outbound_company','cc_dba']
		


class SearchSerializer(serializers.ModelSerializer):
	areas_of_interest=Areas_Of_Interrest_Serializer(many=True)
	callcenter=CallCenterSerializer(many=False)
	class Meta:
		model=Search
		fields="__all__"
		extra_kwargs=extra_kwargs={'id':{'write_only':True, "read_only":False},}
		

class Other_InfoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Other_Info
		fields="__all__"
		

class SearchConnectedSerializer(serializers.ModelSerializer):
	prospect=ProspectSerializer(many=False)
	search=SearchSerializer(many=False)
	other_info=Other_InfoSerializer(many=False)
	class Meta:
		model=SearchConnected
		fields="__all__"


class SearchKeyWordSerializer(serializers.Serializer):
	first_name=serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
	last_name=serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
	email=serializers.EmailField(allow_blank=False, trim_whitespace=True)
