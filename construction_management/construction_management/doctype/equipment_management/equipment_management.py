import frappe
from frappe.model.document import Document

class EquipmentManagement(Document):
    def validate(self):
        self.calculate_consumption_rate()
        self.update_equipment_status()
    
    def calculate_consumption_rate(self):
        """Calculate fuel consumption rate"""
        if self.fuel_consumption:
            for consumption in self.fuel_consumption:
                if consumption.quantity and consumption.hours_operated:
                    consumption.consumption_rate = consumption.quantity / consumption.hours_operated
    
    def update_equipment_status(self):
        """Update equipment status based on maintenance schedule"""
        if self.maintenance_schedule:
            overdue_maintenance = [m for m in self.maintenance_schedule 
                                if m.schedule_date and m.schedule_date < frappe.utils.nowdate() 
                                and m.status in ["Scheduled", "In Progress"]]
            
            if overdue_maintenance:
                self.status = "Under Maintenance"
    
    def on_submit(self):
        """Create Asset record on submit"""
        self.create_asset_record()
    
    def create_asset_record(self):
        """Create Asset record from equipment"""
        asset = frappe.new_doc("Asset")
        asset.asset_name = self.equipment_name
        asset.item_code = self.get_asset_item_code()
        asset.gross_purchase_amount = self.purchase_cost
        asset.purchase_date = self.purchase_date
        asset.location = "Construction Site"
        
        asset.insert()
        
        frappe.msgprint(f"Asset {asset.name} created successfully.")
    
    def get_asset_item_code(self):
        """Get or create asset item code"""
        # This is a simplified version - you might want to enhance this
        item_code = f"EQ-{self.equipment_type}-{self.equipment_name}"
        
        if not frappe.db.exists("Item", item_code):
            item = frappe.new_doc("Item")
            item.item_code = item_code
            item.item_name = self.equipment_name
            item.item_group = "Equipment"
            item.is_fixed_asset = 1
            item.stock_uom = "Nos"
            item.insert()
        
        return item_code