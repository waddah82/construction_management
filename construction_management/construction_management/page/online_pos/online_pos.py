import frappe
from frappe.utils import flt
from collections import defaultdict

def get_context(context):
    context.title = "Animated Pro Online POS"

    context.orders = frappe.get_all(
        "Sales Order",
        filters={"docstatus": 1},
        fields=["name", "customer", "grand_total", "status", "delivery_date", "creation", "items"]
    )

    daily_sales = defaultdict(float)
    for order in context.orders:
        date = order.creation.date()
        daily_sales[date] += flt(order.grand_total)

    context.chart_labels = list(daily_sales.keys())
    context.chart_data = list(daily_sales.values())
