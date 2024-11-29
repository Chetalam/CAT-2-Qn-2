from django.http import JsonResponse
from django.views import View
from .models import Product
import json

class ProductList(View):
    def get(self, request):
        products = Product.objects.all().values()
        return JsonResponse(list(products), safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            product = Product.objects.create(
                name=data['name'],
                description=data['description'],
                price=data['price']
            )
            return JsonResponse({'id': product.id}, status=201)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid input'}, status=400)