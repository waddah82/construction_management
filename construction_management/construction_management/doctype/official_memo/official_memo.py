import frappe
from frappe.model.document import Document

class OfficialMemo(Document):
    def before_insert(self):
        if not self.memo_number:
            self.memo_number = frappe.model.naming.make_autoname("MEMO-.YYYY.-.####")

    