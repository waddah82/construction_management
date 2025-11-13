frappe.ui.form.on('Project Planning', {
    onload(frm) {
        frm.trigger('calculate_totals');
    },
    refresh(frm) {
        frm.add_custom_button(__('Update Total Costs'), () => {
            frm.trigger('calculate_totals');
        });
    },

    calculate_totals(frm) {
        let materials_total = 0;
        let expenses_total = 0;
        let timesheets_total = 0;
        let tasks_total = 0;

        (frm.doc.materials || []).forEach(row => {
            materials_total += flt(row.qty) * flt(row.rate);
        });

        (frm.doc.expenses || []).forEach(row => {
            expenses_total += flt(row.amount);
        });

        (frm.doc.timesheets || []).forEach(row => {
            timesheets_total += flt(row.hours) * flt(row.rate);
        });
        
        (frm.doc.tasks || []).forEach(row => {
            tasks_total += flt(row.estimated_cost);
        });

        const total_cost = materials_total + expenses_total + timesheets_total ;

        frm.set_value('materials_total', materials_total);
        frm.set_value('expenses_total', expenses_total);
        frm.set_value('timesheets_total', timesheets_total);
        frm.set_value('tasks_total', tasks_total);
        frm.set_value('total_cost', total_cost);

        frm.refresh_fields(['materials_total', 'expenses_total', 'timesheets_total', 'tasks_total', 'total_cost']);
    },
});

['Project Planning Material', 'Project Planning Expense', 'Project Planning Timesheet', 'Project Planning Task'].forEach(doctype => {
    frappe.ui.form.on(doctype, {
        amount(frm) { frm.trigger('calculate_totals'); },
        hours(frm) { frm.trigger('calculate_totals'); },
        rate(frm) { frm.trigger('calculate_totals'); },
        estimated_cost(frm) { frm.trigger('calculate_totals'); },
        items_remove(frm) { frm.trigger('calculate_totals'); },
        items_add(frm) { frm.trigger('calculate_totals'); },
        qty_add(frm) { frm.trigger('calculate_totals'); }
    });
});



frappe.ui.form.on('Project Planning1', {
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
