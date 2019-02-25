from __future__ import unicode_literals
import frappe, erpnext
import frappe.defaults
from frappe.utils import cint, flt, fmt_money
from frappe import _, msgprint, throw

@frappe.whitelist()
def get_last_sales_price(item,customer):
	last_sales_price = frappe.db.sql("select rate from `tabSales Invoice Item`,`tabSales Invoice` where `tabSales Invoice Item`.parent = `tabSales Invoice`.name and item_code = '{0}' and customer = '{1}' order by `tabSales Invoice`.creation desc limit 1".format(item,customer),as_dict=1)
	return last_sales_price
