from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from myapi.models import Customer
from .serializers import InfoSerializer
from rest_framework.permissions import IsAuthenticated

class CustomerListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        customer_info = Customer.objects.all()
        serializer = InfoSerializer(customer_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'address': request.data.get('address'),
            'phone': request.data.get('phone')
        }
        serializer = InfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, customer_id):
        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return None

    # 3. retrieve
    def get(self, request, customer_id, *args, **kwargs):
        cus_instance = self.get_object(customer_id)
        if not cus_instance:
            return Response(
                {"res": "object with customer id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = InfoSerializer(cus_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, customer_id, *args, **kwargs):
        cus_instance = self.get_object(customer_id)
        if not cus_instance:
            return Response(
                {"res": "Object with customer id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'address': request.data.get('address'),
            'phone': request.data.get('phone'),
        }

        serializer = InfoSerializer(instance=cus_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        # 5. Delete
        '''
        Deletes the todo item with given cus_id if exists
        '''

    def delete(self, request, customer_id, *args, **kwargs):
        cus_instance = self.get_object(customer_id)
        if not cus_instance:
            return Response(
                {"res": "Object with customer ID does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        cus_instance.delete()
        return Response(
            {"res": "Object deleted"},
            status=status.HTTP_200_OK
        )