from datetime import timedelta
import calendar


def get_date(serializer):
    """Получить данные из сериализатора"""
    data = serializer.validated_data
    data['rate'] = data['rate'] / 12

    return data


def process_data(data):
    """Обработка данных и расчет депозита"""
    amount = data['amount']
    rate = data['rate']
    periods = data['periods']
    current_date = data['date']

    total_data = {}

    for _ in range(periods):
        amount = amount + (amount / 100 * rate)
        total_data[current_date.strftime('%d.%m.%Y')] = round(
            amount, 2
        )
        days_in_next_month = get_amount_days_in_month(
            current_date
        )
        current_date = get_next_date(
            current_date, days_in_next_month
        )

    return total_data


def get_amount_days_in_month(date):
    """Получить количество дней в следующем месяце"""
    if date.month == 12:
        next_month = 1
    else:
        next_month = date.month + 1
    days_in_month = calendar.monthrange(date.year, next_month)[1]
    return days_in_month


def get_next_date(current_date, days):
    """Расчитать следующую дату"""
    next_date = current_date + timedelta(days=days)
    return next_date
