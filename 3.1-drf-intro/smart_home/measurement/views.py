# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer

class CreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        review = SensorDetailSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class ListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class ListCreateAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})