from fcm_django.models import FCMDevice
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_417_EXPECTATION_FAILED
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from advertise.models import category
from advertise.paginaton import custumPaginationClass
from advertise.serializer import categorySerializer
from .models import notification
from .models import subscribe
from .serializer import notificationSerializer


class testDjangoFcm(APIView):
    def get(self, request):
        devices = FCMDevice.objects.all()
        devices.send_message(data={'title': 'it passed', 'body': 'from backend'})
        # devices.send_message(title='it passed',body='from backend')
        return Response({"message": 'done'})


class testGetNot(APIView):
    def get(self, request):
        return Response({
            'message': 'notification retrieved'
        })


class subscribeView(APIView):
    def post(self,request):
        sub,created=subscribe.objects.get_or_create(category_id=request.data.get('id'))
        sub.users.add(request.user)
        user_cat_list=subscribe.objects .filter(users=request.user)
        return Response({'categories_id': [item.id for item in user_cat_list]})

    # permission_classes = (IsAuthenticated,)
    #
    # def get(self, request, *args, **kwargs):
    #     user_subscribe = subscribe.objects.all().filter(users=request.user)
    #     user_category = [item.category for item in user_subscribe]
    #     serializer = categorySerializer(user_category, many=True, context={'request': request})
    #     return Response(serializer.data)
    #
    # def put(self, request, *args, **kwargs):
    #     try:
    #         the_category = category.objects.get(name=request.data.get('category'))
    #         subscrition_item, created = subscribe.objects.get_or_create(category=the_category)
    #         subscrition_item.users.add(request.user)
    #         return Response('subscribed sucssefuly')
    #     except:
    #         return Response('ERORR:  category name or users token ', status=HTTP_417_EXPECTATION_FAILED)
    #
    # def delete(self, request, *args, **kwargs):
    #     try:
    #         the_category = category.objects.get(name=request.data.get('category'))
    #         subscrition_item, created = subscribe.objects.get_or_create(category=the_category)
    #         subscrition_item.users.remove(request.user)
    #         return Response('subscribed done')
    #     except:
    #         return Response('Error:  category name or users token ', status=HTTP_417_EXPECTATION_FAILED)


class subscribedCategory(APIView):
    def get(self, request):
        categories = subscribe.objects.filter(users=request.user)
        categories_id = [item.id for item in categories]
        return Response({'categories_id': categories_id})


class getUserNotification(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    pagination_class = custumPaginationClass
    serializer_class = notificationSerializer

    def get_queryset(self, ):
        return notification.objects.filter(user=self.request.user).order_by('-id')

    def retrieve(self, request, pk=None):
        try:
            notes = notification.objects.all()
            notes.filter(id=pk).update(seen=True)
            noteCount = notification.objects.filter(user=request.user).filter(seen=False).count()
            return Response({'notificationCount': str(noteCount), 'pk': pk})
        except:
            return Response('readed')

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        numberOfNotifications = str(self.get_queryset().filter(seen=False).count())
        response.data['notificationCount'] = numberOfNotifications

        return response


class RegisterDevice(APIView):
    def post(self, request):
        user = request.user
        FCM = request.data.get('FCM', None)
        if user and FCM:
            FCMDevice.objects.update_or_create(defaults={"registration_id": FCM}, user=user)
            return Response({"message": "working"})
        else:
            return Response({"error": "invalid FCM or User"}, status=status.HTTP_400_BAD_REQUEST)
