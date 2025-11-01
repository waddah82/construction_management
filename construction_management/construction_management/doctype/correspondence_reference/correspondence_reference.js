frappe.ui.form.on('Correspondence Reference', {
    reference_doctype: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.reference_doctype) {
            frappe.call({
                method: "frappe.client.get_list",
                args: {
                    doctype: row.reference_doctype,
                    fields: ["name"],
                    limit_page_length: 20
                },
                callback: function(r) {
                    if (r.message) {
                        console.log("Available docs:", r.message);
                    }
                }
            });
        }
    },

    reference_document: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.reference_doctype && row.reference_document) {
            frappe.call({
                method: "frappe.client.get_value",
                args: {
                    doctype: row.reference_doctype,
                    filters: { name: row.reference_document },
                    fieldname: ["workflow_state", "docstatus"]
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.model.set_value(cdt, cdn, "workflow_state", r.message.workflow_state || "");
                        let doc_status_map = {0: "Draft", 1: "Submitted", 2: "Cancelled"};
                        frappe.model.set_value(cdt, cdn, "doc_status", doc_status_map[r.message.docstatus] || "");
                    }
                }
            });
        }
    }
});
