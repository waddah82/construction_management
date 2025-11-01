import frappe
from frappe.model.document import Document

class CorrespondenceReference(Document):
    def before_insert(self):
        if self.user and not frappe.db.exists("User", self.user):
            frappe.throw(f"User {self.user} does not exist")

    def validate(self):
    
        if not self.doc_status:
            self.doc_status = "Draft"


        if not self.workflow_state:
            self.workflow_state = "Pending"
