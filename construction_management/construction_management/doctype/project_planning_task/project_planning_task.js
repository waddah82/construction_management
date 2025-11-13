frappe.ui.form.on('Project Planning Task', {
    create_task_button(frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        frappe.new_doc('Task', {
            project: frm.doc.project,
            subject: row.task_name,
            description: row.description,
            exp_start_date: row.expected_start_date,
            exp_end_date: row.expected_end_date,
            estimated_time: row.estimated_hours,
            status: 'Open'
        });
    }
});
