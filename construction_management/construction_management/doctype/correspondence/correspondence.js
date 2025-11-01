
frappe.ui.form.on('Correspondence', {
    onload: function(frm) {
        if (frm.doc && !frm.doc.__islocal) return;
        if (frm.fields_dict && frm.set_value) {
            if (frm.doc && !frm.doc.name) {
                if (frm.fields_dict['entry_date']) {
                    frm.set_value('entry_date', frappe.datetime.get_today());
                }
            }
        }
    },

    refresh: function(frm) {
        if (!frm.is_new()) {
            if (frm.doc && frm.doc.status == 'Archived') {
                frm.disable_form();
            }

            frm.add_custom_button(__('Reply'), function() {
                let new_doc = frappe.model.get_new_doc('Correspondence');
                new_doc.reply_to = frm.doc.name;

                if (frm.doc.naming_series) {
                    new_doc.naming_series = frm.doc.naming_series;
                }

                new_doc.sender = frm.doc.sender;
                new_doc.receiver = frm.doc.receiver;
                new_doc.priority = frm.doc.priority;
                new_doc.status = 'Draft';
                new_doc.title = frm.doc.title;
                new_doc.correspondence_date = frm.doc.correspondence_date;
                new_doc.correspondence_type = frm.doc.correspondence_type;
                new_doc.entry_date = frappe.datetime.nowdate();

                if (frm.doc.reference_table && frm.doc.reference_table.length) {
                    frm.doc.reference_table.forEach(function(r) {
                        let row = frappe.model.add_child(new_doc, 'reference_table', 'reference_table');
                        row.reference_doctype = r.reference_doctype;
                        row.reference_document = r.reference_document;
                        row.document_status = r.document_status;
                        row.user = r.user;
                    });
                }

                if (frm.doc.related_contacts && frm.doc.related_contacts.length) {
                    frm.doc.related_contacts.forEach(function(c) {
                        let row = frappe.model.add_child(new_doc, 'related_contacts', 'related_contacts');
                        row.contact_name = c.contact_name;
                        row.designation = c.designation;
                        row.department = c.department;
                        row.email = c.email;
                        row.phone = c.phone;
                    });
                }

                frappe.set_route('Form', 'Correspondence', new_doc.name);

                frappe.ui.form.on('Correspondence', 'after_save', function(new_frm) {
                    if (new_frm.doc.reply_to) {
                        frappe.db.set_value(
                            'Correspondence',
                            new_frm.doc.reply_to,
                            'latest_reply',
                            new_frm.doc.name
                        ).then(() => {
                            frappe.msgprint(__('Original document updated with latest reply'));
                        });
                    }
                });

            }, __('Add'));

            frm.add_custom_button(__('Add Related Document'), function() {
                frappe.prompt([
                    {
                        fieldname: 'reference_doctype',
                        fieldtype: 'Link',
                        label: 'Reference Doctype',
                        options: 'DocType',
                        reqd: 1
                    },
                    {
                        fieldname: 'reference_document',
                        fieldtype: 'Dynamic Link',
                        label: 'Reference Document',
                        options: 'reference_doctype',
                        reqd: 1
                    },
                    {
                        fieldname: 'document_status',
                        fieldtype: 'Data',
                        label: 'Document Status'
                    }
                ],
                function(values) {
                    let row_values = {
                        reference_doctype: values.reference_doctype,
                        reference_document: values.reference_document,
                        document_status: values.document_status,
                        user: frappe.session.user
                    };

                    frm.add_child('reference_table', row_values);
                    frm.refresh_field('reference_table');

                    frappe.msgprint(__('Related Document Added'));
                });

            }, __('Add'));    
        }
    }
});
