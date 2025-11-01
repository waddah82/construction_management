frappe.ui.form.on('Project Planning', {
    refresh(frm) {
        // زر إنشاء مهام
        frm.add_custom_button(__('Create Tasks'), () => {
            frappe.call({
                method: "secretaria.secretaria.doctype.project_planning.project_planning.create_tasks",
                args: { doc: frm.doc },
                callback: function () { frappe.msgprint("✅ Tasks Created"); }
            });
        });

        // زر إنشاء التايم شيت
        frm.add_custom_button(__('Create Timesheets'), () => {
            frappe.call({
                method: "secretaria.secretaria.doctype.project_planning.project_planning.create_timesheets",
                args: { doc: frm.doc },
                callback: function () { frappe.msgprint("✅ Timesheets Created"); }
            });
        });

        // زر إنشاء Expense Claims
        frm.add_custom_button(__('Create Expense Claims'), () => {
            frappe.call({
                method: "secretaria.secretaria.doctype.project_planning.project_planning.create_expenses",
                args: { doc: frm.doc },
                callback: function () { frappe.msgprint("✅ Expense Claims Created"); }
            });
        });

        // زر إنشاء Material Request
        frm.add_custom_button(__('Create Material Requests'), () => {
            frappe.call({
                method: "secretaria.secretaria.doctype.project_planning.project_planning.create_material_requests",
                args: { doc: frm.doc },
                callback: function () { frappe.msgprint("✅ Material Requests Created"); }
            });
        });
    }
});
