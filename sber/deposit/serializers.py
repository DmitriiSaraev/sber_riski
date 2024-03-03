from rest_framework import serializers


# {
#     "date": "31.01.2021",
#     "periods": 3,
#     "amount": 10000,
#     "rate": 6
# }

# {
#     "31.01.2021": 10050,
#     "28.02.2021": 10100.25,
#     "31.03.2021": 10150.75,
# }


class DepositSerializer(serializers.Serializer):
    date = serializers.DateField(input_formats=["%d.%m.%Y"])
    periods = serializers.IntegerField(min_value=1, max_value=60)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2,
                                      min_value=10000, max_value=3000000)
    rate = serializers.DecimalField(max_digits=3, decimal_places=2,
                                    min_value=1, max_value=8)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass