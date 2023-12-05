from core.models import CalculationResult
from django.shortcuts import render
from django.http import Http404


def calculation_result(request, result_id):
    try:
        result = CalculationResult.objects.get(pk=result_id)
    except CalculationResult.DoesNotExist:
        raise Http404("Result not found.")

    return render(request, "core/calculation_result.html", {"result": result})
