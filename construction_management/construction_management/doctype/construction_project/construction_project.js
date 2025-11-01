frappe.ui.form.on('Construction Project', {
    refresh: function(frm) {
        // Add custom button to create material requisition
        frm.add_custom_button(__('Create Material Requisition'), function() {
            frappe.model.open_mapped_doc({
                method: "construction_management.construction_management.doctype.construction_project.construction_project.create_material_requisition",
                frm: frm
            });
        });
    },
    
    calculate_totals: function(frm) {
        // Calculate total budget and actual cost
        let total_budget = 0;
        let actual_cost = 0;
        
        if (frm.doc.construction_stages) {
            frm.doc.construction_stages.forEach(function(stage) {
                total_budget += stage.stage_budget || 0;
                actual_cost += stage.actual_cost || 0;
            });
        }
        
        frm.set_value('total_budget', total_budget);
        frm.set_value('actual_cost', actual_cost);
    }
});

frappe.ui.form.on('Construction Stage', {
    construction_stages_add: function(frm, cdt, cdn) {
        frm.trigger('calculate_totals');
    },
    construction_stages_remove: function(frm, cdt, cdn) {
        frm.trigger('calculate_totals');
    },
    stage_budget: function(frm, cdt, cdn) {
        frm.trigger('calculate_totals');
    },
    actual_cost: function(frm, cdt, cdn) {
        frm.trigger('calculate_totals');
    }
});