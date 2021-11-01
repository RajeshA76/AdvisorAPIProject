from .models import User
from rest_framework import generics,status
from admin_role.models import AdvisorModel
from .serializers import AdvisorListSerializer, BookingListSerializer,LoginSerializer, RegisterSerializer,BookedCallsSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
import re
from .models import Booking
from rest_framework.views import APIView
from django.contrib.auth import login


# Create your views here.

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            context = {'id': serializer.data['id'],'token': "login to creat JWT Token"}
            return Response(data=context,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        
class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        print(email)
        print(password)


        if email and password:
            print("error")
            user_auth = authenticate(username=email,password=password)
            if user_auth:
                print("inside")
                serializer = self.serializer_class(user_auth)
                context = {'id':serializer.data['id'],'token':serializer.data['token']}
                return Response(data=context,status=status.HTTP_200_OK) 
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



# class AdvisorList(generics.ListAPIView):

#     serializer_class = AdvisorListSerializer
#     lookup_url_kwarg = "id"
#     advisor_data = AdvisorModel.objects.all()
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         queryset = AdvisorModel.objects.all()
#         print(dir(queryset))
#         url_id = self.kwargs.get(self.lookup_url_kwarg)
#         uid = "UUID('"+str(url_id)+")"
#         all_data = User.objects.all()
#         list_uuid = [i.id for i in all_data]
#         if uid in list_uuid:
#             serializer = self.serializer_class(queryset.data)
#             return Response(data=serializer.data,status=status.HTTP_200_OK)

# def displayData(request,id):
#     all_data = User.objects.all()
#     list_uuid = [i.id for i in all_data]

#     if id in list_uuid:
#         data = AdvisorModel.objects.all()
#         post_list = serializers.serialize('json',
#                                             list(data),
#                                             fields=('AdvisorName','AdvisorPhotoUrl'))
#         return HttpResponse(post_list,status=200)

class AdvisorListView(APIView):

    def get(self,request,id):
        all_data = User.objects.all()
        list_uuid = [i.id for i in all_data]
        if id in list_uuid:
            obj = AdvisorModel.objects.all()
            serializer = AdvisorListSerializer(obj,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)




class BookingView(generics.GenericAPIView):

    serializer_class = BookedCallsSerializer


    def post(self,request,id,advisor_id):

        all_data = User.objects.all()
        list_uuid = [i.id for i in all_data]
    
        if id in list_uuid:

            pattern = '[0-3]\d\/[0-1]\d\/\d\d\d\d\s([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
            

            try:
                match = re.search(pattern,request.data['BookingTime'])
                if match:
                    print(True)
                    context = {'uid':id,'advisor_id':advisor_id,'BookingTime':request.data['BookingTime']}
                    serializer = self.serializer_class(data=context)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
              
            except:
                return Response(data="Provide BookingTime key with value as DD/MM/YYYY HR:MIN",status=status.HTTP_400_BAD_REQUEST)

class BookedCallsView(APIView):

    def get(self,request,id):
        
        obj = Booking.objects.filter(uid=id)
        serializer = BookingListSerializer(obj,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)