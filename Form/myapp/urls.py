from django.urls import path
from .views import EnquiryListCreate,EnquiryRetrieveUpdateDestroy

urlpatterns = [
    path('enquiries/', EnquiryListCreate.as_view(), name='enquiry-list-create'),
    path('enquiries/<int:pk>/', EnquiryRetrieveUpdateDestroy.as_view(), name='enquiry-detail')
]
