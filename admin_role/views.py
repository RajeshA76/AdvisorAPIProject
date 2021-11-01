from django.shortcuts import render
from rest_framework import generics,status
from .serializers import AdvisorSerializer
from rest_framework.response import Response




# Create your views here.
class AdvisorView(generics.GenericAPIView):

    serializer_class = AdvisorSerializer
    def post(self,request):
        advisor = request.data
        serializer = self.serializer_class(data=advisor)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            return Response(user_data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

		