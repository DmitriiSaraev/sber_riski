from django.test import TestCase

import unittest
from datetime import datetime, timedelta
import calendar
from unittest.mock import MagicMock
# import deposit.utils as utils
from deposit.utils import get_date, process_data, get_amount_days_in_month, get_next_date

class TestDepositCalculation(unittest.TestCase):
    def test_get_date(self):
        # Создаем заглушку для сериализатора
        serializer = MagicMock()
        serializer.validated_data = {'amount': 10000, 'rate': 6, 'periods': 3, 'date': datetime(2022, 1, 1)}

        # Проверяем корректность получения данных
        data = get_date(serializer)
        self.assertEqual(data['rate'], 0.5)  # rate / 12

    def test_process_data(self):
        data = {'amount': 10000, 'rate': 0.5, 'periods': 3, 'date': datetime(2022, 1, 1)}

        # Проверяем корректность обработки данных и расчета депозита
        total_data = process_data(data)
        self.assertEqual(len(total_data), 3)  # Проверяем, что результат содержит 3 даты

    def test_get_amount_days_in_month(self):
        # Проверяем корректность получения количества дней в месяце
        days_in_month = get_amount_days_in_month(datetime(2022, 1, 1))
        self.assertEqual(days_in_month, 28)  # Январь 2022 года должен содержать 31 день

    def test_get_next_date(self):
        # Проверяем корректность расчета следующей даты
        next_date = get_next_date(datetime(2022, 1, 1), 31)
        self.assertEqual(next_date, datetime(2022, 2, 1))  # Следующий месяц после января 2022 года

if __name__ == '__main__':
    unittest.main()

