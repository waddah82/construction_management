frappe.ui.form.on('Project Planning Expense', {
    create_ec_button(frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        frappe.new_doc('Expense Claim', {
            employee: row.employee,
            project: frm.doc.project,
            expenses: [{
                expense_type: row.expense_type,
                description: row.description,
                amount: row.amount
            }]
        });
    }
});
