from frappe import _
def custom_get_dashboard_data():
	return {
		"fieldname": "task",
		"transactions": [
			{"label": _("Project"), "items": ["Project"]},
			{"label": _("Activity"), "items": ["Timesheet"]},
			{"label": _("Material"), "items": ["Material Request", "BOM", "Stock Entry"]},
			{"label": _("Sales"), "items": ["Sales Order", "Delivery Note", "Sales Invoice"]},
			{"label": _("Purchase"), "items": ["Purchase Order", "Purchase Receipt", "Purchase Invoice"]},
		],
	}
