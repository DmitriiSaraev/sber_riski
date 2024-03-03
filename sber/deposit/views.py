from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime, timedelta
import calendar

from deposit.serializers import DepositSerializer


class DepositCalculationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DepositSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            amount = data['amount']
            rate = data['rate'] / 12
            periods = data['periods']
            current_date = data['date']

            total_data = {}

            for _ in range(periods):
                amount = amount + (amount / 100 * rate)
                total_data[current_date.strftime('%d.%m.%Y')] = round(
                    amount, 2
                )
                days_in_next_month = get_amount_days_in_month(current_date)
                current_date = get_next_date(current_date, days_in_next_month)
            return Response(total_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )


def get_amount_days_in_month(date):
    if date.month == 12:
        next_month = 1
    else:
        next_month = date.month + 1
    days_in_month = calendar.monthrange(date.year, next_month)[1]
    return days_in_month


def get_next_date(current_date, days):
    next_date = current_date + timedelta(days=days)
    return next_date
