from django.shortcuts import render , redirect
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework import generics 
from django.http import Http404
from rest_framework.views import APIView
from . serializers import SearchConnectedSerializer,SearchKeyWordSerializer
from . models import SearchConnected, Prospect

# Create your views here.

class SearchConnectedView(generics.ListAPIView):
	queryset=SearchConnected.objects.all()
	serializer_class=SearchConnectedSerializer
	# permission_classes=[IsAuthenticated]


class SearchConnectedView_(APIView):
	# queryset=SearchConnected.objects.all()
	serializer_class=SearchKeyWordSerializer
	permission_classes=[IsAuthenticated]

	def get(self, request, *args, **kwargs):
		queryset=SearchConnected.objects.all()
		serializer = SearchConnectedSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):

		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		print(first_name,last_name,email)
		try:
			prospect=Prospect.objects.get(first_name=first_name, last_name=last_name, email=email)
		except:
			return Response("No matching query, visit domain/v3/ to see all data from the database")

		result=SearchConnected.objects.get(prospect=prospect)
		serializer=SearchConnectedSerializer(result, many=False)
		return redirect("result", result.pk)
		# return Response(serializer.data)

class ResultConnectedView_(generics.RetrieveAPIView):
	queryset=SearchConnected.objects.all()
	serializer_class=SearchConnectedSerializer
	permission_classes=[IsAuthenticated]
