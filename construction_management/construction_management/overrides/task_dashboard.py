from frappe import _
def custom_get_dashboard_data(data=None):
	return {
		"fieldname": "task",
		"transactions": [
			{"label": _("Timesheets"), "items": ["Timesheet"]},
			{"label": _("Material"), "items": ["Material Request", "Stock Entry"]},
			{"label": _("Sales"), "items": ["Sales Order", "Delivery Note", "Sales Invoice"]},
			{"label": _("Purchase"), "items": ["Purchase Order", "Purchase Receipt", "Purchase Invoice"]},
		],
	}
