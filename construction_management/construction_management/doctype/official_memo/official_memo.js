frappe.ui.form.on('Official Memo', {
    refresh: function(frm) {
        if (!frm.is_new() && frm.doc.status !== "Draft") {
            frm.add_custom_button(__('?? Print Memo'), function() {
                frappe.ui.form.make_printable(frm);
            });
        }

        if (frm.doc.status === "Draft" && !frm.is_new()) {
            frm.add_custom_button(__('Issue Memo'), function() {
                frm.set_value("status", "Issued");
                frm.save();
            }, __("Status"));
        }
    }
});