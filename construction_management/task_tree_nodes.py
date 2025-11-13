# construction_management/construction_management/projects_custom/task_tree_nodes.py

import frappe
from frappe import _

@frappe.whitelist()
def get_custom_task_children(doctype, parent, task=None, project=None, is_root=False):
    """
    تجلب المهام الأبناء، بالإضافة إلى Timesheet, Expense Claim, و Material Request المرتبطة.
    """
    
    # تحديد المهمة الحالية (Task ID)
    current_task_id = task if task else parent

    # 1. جلب المهام الأبناء القياسية
    filters = [["docstatus", "<", "2"]]

    if current_task_id and current_task_id not in ("All Tasks", "None", None, 'null'):
        filters.append(["parent_task", "=", current_task_id])
    elif not is_root:
        filters.append(["parent_task", "=", parent])
    else:
        filters.append(['ifnull(`parent_task`, "")', "=", ""])
        
    if project:
        filters.append(["project", "=", project])

    tasks = frappe.get_list(
        doctype,
        fields=["name as value", "subject as title", "is_group as expandable"],
        filters=filters,
        order_by="name",
    )
    
    # 2. إضافة الوثائق المرتبطة إذا كانت العقدة الحالية هي Task
    if current_task_id and current_task_id not in ("All Tasks", "None", None, 'null'):
        
        # أ. جلب Timesheet (عبر Time Log Detail)
        time_logs = frappe.get_all(
            "Timesheet Detail",
            filters={"task": current_task_id, "docstatus": 1},
            fields=["parent as value", "parent as title", "0 as expandable"],
            distinct=True
        )
        for log in time_logs:
            log["doctype"] = "Timesheet"
            log["title"] = _("Timesheet") + " - " + log["title"]
            log["is_leaf"] = True
            tasks.append(log)

        # ب. جلب Expense Claim (عبر Expense Claim Detail)
        expense_claims = frappe.get_all(
            "Expense Claim Detail",
            filters={"task": current_task_id, "docstatus": 1},
            fields=["parent as value", "parent as title", "0 as expandable"],
            distinct=True
        )
        for claim in expense_claims:
            claim["doctype"] = "Expense Claim"
            claim["title"] = _("Expense Claim") + " - " + claim["title"]
            claim["is_leaf"] = True
            tasks.append(claim)

        # ج. جلب Material Request (يفترض حقل 'task' في MR)
        material_requests = frappe.get_list(
            "Material Request",
            filters={"task": current_task_id, "docstatus": 1},
            fields=["name as value", "name as title", "0 as expandable"],
            order_by="name",
        )
        for req in material_requests:
            req["doctype"] = "Material Request"
            req["title"] = _("Material Request") + " - " + req["title"]
            req["is_leaf"] = True
            tasks.append(req)
            
    return tasks