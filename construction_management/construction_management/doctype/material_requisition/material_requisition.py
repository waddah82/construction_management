import frappe
from frappe.model.document import Document

class MaterialRequisition(Document):
    def validate(self):
        self.calculate_total_cost()
        self.update_status_based_on_dates()
    
    def calculate_total_cost(self):
        """Calculate total estimated cost from items"""
        total = 0
        if self.material_items:
            for item in self.material_items:
                if item.estimated_amount:
                    total += item.estimated_amount
                elif item.quantity and item.estimated_rate:
                    item.estimated_amount = item.quantity * item.estimated_rate
                    total += item.estimated_amount
        self.total_estimated_cost = total
    
    def update_status_based_on_dates(self):
        """Update status based on required date"""
        if self.required_date and self.required_date < frappe.utils.nowdate():
            if self.status in ["Draft", "Submitted"]:
                self.status = "Delayed"
    
    def on_submit(self):
        """Create Material Request on submit"""
        self.create_material_request()
    
    def create_material_request(self):
        """Create Material Request from requisition"""
        material_request = frappe.new_doc("Material Request")
        material_request.material_request_type = "Purchase"
        material_request.schedule_date = self.required_date
        
        for item in self.material_items:
            material_request.append("items", {
                "item_code": item.item_code,
                "qty": item.quantity,
                "uom": item.uom,
                "warehouse": item.warehouse
            })
        
        material_request.insert()
        material_request.submit()
        
        frappe.msgprint(f"Material Request {material_request.name} created successfully.")