import frappe
from frappe.model.document import Document

class ConstructionProject(Document):
    def validate(self):
        self.update_project_status()
        self.calculate_actual_cost()
    
    def update_project_status(self):
        """Update project status based on stages"""
        if not self.construction_stages:
            return
        
        completed_stages = [stage for stage in self.construction_stages if stage.status == "Completed"]
        in_progress_stages = [stage for stage in self.construction_stages if stage.status == "In Progress"]
        
        if len(completed_stages) == len(self.construction_stages):
            self.project_status = "Completed"
        elif in_progress_stages or completed_stages:
            self.project_status = "In Progress"
    
    def calculate_actual_cost(self):
        """Calculate total actual cost from all stages"""
        total_actual_cost = 0
        if self.construction_stages:
            for stage in self.construction_stages:
                if stage.actual_cost:
                    total_actual_cost += stage.actual_cost
        self.actual_cost = total_actual_cost

    def on_submit(self):
        """Actions when project is submitted"""
        frappe.msgprint(f"Project {self.project_name} has been submitted successfully.")

    def on_cancel(self):
        """Actions when project is cancelled"""
        frappe.msgprint(f"Project {self.project_name} has been cancelled.")