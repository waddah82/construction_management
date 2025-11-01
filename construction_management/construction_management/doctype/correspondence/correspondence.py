import frappe
from frappe.model.document import Document
from frappe.desk.doctype.notification_log.notification_log import enqueue_create_notification

class Correspondence(Document):
    pass 
    
def notify_on_new_correspondence(doc, method):
    # notify Secretaries
    users = frappe.get_all('Has Role', filters={'role': 'Secretary'}, fields=['parent'])
    receivers = [u.parent for u in users]
    for r in receivers:
        try:
            enqueue_create_notification(doctype=doc.doctype, name=doc.name, document=doc, notify_by_email=0, user=r)
        except Exception:
            frappe.logger().exception('notify_on_new_correspondence failed')

def on_correspondence_update(doc, method):
    frappe.logger().info(f"Correspondence {doc.name} updated by {doc.modified_by}")