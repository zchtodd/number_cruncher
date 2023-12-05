from django.urls import path
from .views.fibonacci import fibonacci
from .views.calculation import calculation_result

urlpatterns = [
    path("fibonacci/", fibonacci, name="fibonacci"),
    path(
        "calculation/<int:result_id>/result/",
        calculation_result,
        name="calculation_result",
    ),
]
