import frappe
from frappe.model.document import Document

class SubcontractorManagement(Document):
    def validate(self):
        self.calculate_overall_rating()
        self.update_subcontractor_status()
    
    def calculate_overall_rating(self):
        """Calculate overall rating from performance ratings"""
        if self.performance_rating:
            total_rating = 0
            count = 0
            
            for rating in self.performance_rating:
                if rating.overall_rating:
                    total_rating += rating.overall_rating
                    count += 1
            
            if count > 0:
                self.overall_rating = total_rating / count
    
    def update_subcontractor_status(self):
        """Update status based on performance and agreements"""
        if self.performance_rating:
            recent_ratings = sorted(self.performance_rating, 
                                  key=lambda x: x.rating_date, 
                                  reverse=True)[:3]
            
            low_ratings = [r for r in recent_ratings if r.overall_rating and r.overall_rating < 3]
            
            if len(low_ratings) >= 2:
                self.status = "Suspended"
    
    def on_submit(self):
        """Create Supplier record if not exists"""
        self.ensure_supplier_exists()
    
    def ensure_supplier_exists(self):
        """Ensure supplier record exists"""
        if not frappe.db.exists("Supplier", self.subcontractor_name):
            supplier = frappe.new_doc("Supplier")
            supplier.supplier_name = self.subcontractor_name
            supplier.supplier_type = "Subcontractor"
            supplier.supplier_group = "Subcontractors"
            supplier.insert()
            
            frappe.msgprint(f"Supplier {supplier.name} created successfully.")