from django.http import JsonResponse
from django.db.models import (
    F, Func, Value, CharField, Max, Min, Sum, Count
)
from ..models import OrderItem

def get_orders(request):
    objects = list(OrderItem.objects.values(
        'order__supplier', 'quantity', 'unit_price', 'product', 
        subtotal=F('quantity') * F('unit_price'),
    )[:10])

    return JsonResponse({"data": objects}, status=200)


def get_transaction_history(request, product_id):
    query_params = request.GET
    supplier_id = query_params.get('supplier')
    start_date = query_params.get('startDate')
    end_date = query_params.get('endDate')

    filters = {
        "product": product_id,
        "order__supplier__productsupply__product": product_id,
    }

    # Filters
    if supplier_id:
        filters["order__supplier"] = supplier_id
    if start_date:
        filters["order__order_date__gte"] = start_date
    if end_date:
        filters["order__order_date__lte"] = end_date

    order_items_qset = OrderItem.objects.filter(
        **filters
    )

    tx_history = order_items_qset.order_by(
        "order__order_date"
    ).values(
        'order',
        'quantity',
        'unit_price',
        supplier_id=F('order__supplier'),
        supplier_name=F('order__supplier__name'),
        supplier_code=F('order__supplier__code'),
        subtotal=F('quantity') * F('unit_price'),
        order_date=Func(
            F('order__order_date'),
            Value('YYYY-MM-DD HH:mm'),
            function='to_char',
            output_field=CharField()
        ),
    )

    stats = order_items_qset.aggregate(
        max_price = Max('unit_price'),
        min_price = Min('unit_price'),
        total_quantity = Sum('quantity'),
        total_amount = Sum(F('quantity') * F('unit_price')),
        # average_price = (F('min_price') + F('max_price')) / 2,
        average_price = Sum(F('unit_price')) / Count(F('unit_price')),
        overall_average_price = F('total_amount') / F('total_quantity'),
    )

    supplier_stats = order_items_qset.values(
        supplier_id=F('order__supplier__id'),
        name=F('order__supplier__name'),
        code=F('order__supplier__code'),
        current_price=F('order__supplier__productsupply__unit_price'),
    ).annotate(
        max_price = Max('unit_price'),
        min_price = Min('unit_price'),
        total_quantity = Sum('quantity'),
        total_amount = Sum(F('quantity') * F('unit_price')),
        # average_price = (F('min_price') + F('max_price')) / 2,
        average_price = Sum(F('unit_price')) / Count(F('unit_price')),
        overall_average_price = F('total_amount') / F('total_quantity'),
    ).order_by("overall_average_price")

    return JsonResponse({
        "stats": stats,
        "tx_history": list(tx_history),
        "suppliers": list(supplier_stats),
    }, status=200)