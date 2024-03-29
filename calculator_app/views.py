from django.http import JsonResponse
import json
from .calculator import evaluate_expression
from django.shortcuts import redirect, render


def calculate(request):
    if request.method == 'GET':
        return render(request, "calculator.html")

    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        expression = data.get('expression', '')

        try:
            result = evaluate_expression(expression)
            return JsonResponse({'result': result, 'error': None})
        except Exception as e:
            return JsonResponse({'result': None, 'error': str(e)})

    return JsonResponse({'error': 'Invalid request'}, status=400)
