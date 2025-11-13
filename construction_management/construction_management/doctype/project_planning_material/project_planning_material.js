frappe.ui.form.on('Project Planning Material', {
    create_mr_button(frm, cdt, cdn) {
        let row = locals[cdt][cdn];

        frappe.new_doc('Material Request', {
            material_request_type: 'Purchase',
            company: frm.doc.company,
            items: [{
                item_code: row.item_code,
                item_name: row.item_name,
                description: row.description,
                uom: row.uom,
                qty: row.qty,
                rate: row.rate
            }]
        });
    }
});
