frappe.ui.form.on('Project Planning Timesheet', {
    create_ts_button(frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        frappe.new_doc('Timesheet', {
            employee: row.employee,
            time_logs: [{
                activity_type: row.activity_type,
                task: row.task,
                hours: row.hours,
                billing_rate: row.rate,
                project: frm.doc.project
            }]
        });
    }
});
