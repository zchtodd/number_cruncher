from celery import shared_task
from core.models import CalculationResult


@shared_task(queue="fibonacci")
def calculate_fibonacci(result_id, n):
    def fibonacci(num):
        if num <= 1:
            return num
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

    result = fibonacci(n)

    calculation_result = CalculationResult.objects.get(pk=result_id)
    calculation_result.result = result
    calculation_result.save()

    return result


@shared_task(queue="prime")
def calculate_nth_prime(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if num < 2:
            continue
        if any(num % i == 0 for i in range(2, int(num**0.5) + 1)):
            continue
        count += 1

    return num
