frappe.ui.form.on('Material Requisition', {
    refresh: function(frm) {
        // Add custom button to create purchase order
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__('Create Purchase Order'), function() {
                frappe.model.open_mapped_doc({
                    method: "construction_management.construction_management.doctype.material_requisition.material_requisition.create_purchase_order",
                    frm: frm
                });
            });
        }
    }
});

frappe.ui.form.on('Material Requisition Item', {
    quantity: function(frm, cdt, cdn) {
        calculate_item_amount(frm, cdt, cdn);
    },
    estimated_rate: function(frm, cdt, cdn) {
        calculate_item_amount(frm, cdt, cdn);
    },
    material_items_remove: function(frm) {
        calculate_total_amount(frm);
    }
});

function calculate_item_amount(frm, cdt, cdn) {
    var row = locals[cdt][cdn];
    if (row.quantity && row.estimated_rate) {
        frappe.model.set_value(cdt, cdn, 'estimated_amount', row.quantity * row.estimated_rate);
    }
    calculate_total_amount(frm);
}

function calculate_total_amount(frm) {
    var total = 0;
    $.each(frm.doc.material_items || [], function(i, item) {
        total += item.estimated_amount || 0;
    });
    frm.set_value('total_estimated_cost', total);
}