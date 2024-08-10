
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Enquiry
from .serializer import EnquirySerializer
class EnquiryListCreate(generics.ListCreateAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    def get(self, request):
        enquiries = Enquiry.objects.all()
        serializer = EnquirySerializer(enquiries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnquiryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Enquiry
# from .serializer import EnquirySerializer

# class EnquiryListCreate(APIView):
#     def get(self, request):
#         enquiries = Enquiry.objects.all()
#         serializer = EnquirySerializer(enquiries, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EnquirySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
