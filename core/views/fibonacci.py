from django.shortcuts import render
from django.http import HttpResponse

from core.forms import FibonacciForm
from core.models import CalculationResult

from core.tasks import calculate_fibonacci


def fibonacci(request):
    if request.method == "POST":
        form = FibonacciForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]

            result = CalculationResult()
            result.save()

            calculate_fibonacci.delay(result.id, number)
            return render(request, "core/calculation_result.html", {"result": result})
    else:
        form = FibonacciForm()
    return render(request, "core/fibonacci_form.html", {"form": form})
