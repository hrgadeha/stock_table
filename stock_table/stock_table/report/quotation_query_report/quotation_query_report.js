// Copyright (c) 2016, Hardik Gadesha and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Quotation Query Report"] = {
	"filters": [
		{
		    "fieldname": "customer",
	            "label": __("Select Customer"),
	            "fieldtype": "Link",
		    "options": "Customer"
		},
		{
		    "fieldname": "item",
	            "label": __("Select Item"),
	            "fieldtype": "Link",
		    "options": "Item"
		}
	]
}
