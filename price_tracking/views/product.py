from django.http import JsonResponse
from ..models import Product

def get_products(request):
    clients = list(Product.objects.values())

    return JsonResponse({"products": clients}, status=200)

