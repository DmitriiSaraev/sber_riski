from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime, timedelta
import calendar

from deposit.serializers import DepositSerializer
import deposit.utils as utils


class DepositCalculationView(APIView):
    """Получаем валидированные данные, обрабатываем и отдаем ответ
    Производим расчет депозита.
    """
    def post(self, request, *args, **kwargs):
        serializer = DepositSerializer(data=request.data)

        if serializer.is_valid():
            data = utils.get_date(serializer)
            total_data = utils.process_data(data)

            return Response(total_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

