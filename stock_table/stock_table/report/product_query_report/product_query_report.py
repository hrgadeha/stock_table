# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = get_column()
	data = get_data(filters)
	return columns,data

def get_column():
	return [_("Item Code") + ":Data:180",_("Item Name") + ":Data:180",_("Discription") + ":Data:180",_("Sales Price") + ":Float:100",_("Wholesale Price") + ":Float:100",_("Last Sale Price") + ":Float:100",_("Last Purchase Price") + ":Float:100"]

def get_data(filters):
	if filters.get("item"):
		item = filters.get("item")	
		item_data = frappe.db.sql("""select item_code, item_name, description, standard_rate, wholesale_rate , 
(select rate from `tabSales Invoice Item`,`tabSales Invoice` 
where `tabSales Invoice Item`.parent = `tabSales Invoice`.name and item_code = '{0}'  
order by `tabSales Invoice`.creation desc limit 1),
(select rate from `tabPurchase Invoice Item`,`tabPurchase Invoice` 
where `tabPurchase Invoice Item`.parent = `tabPurchase Invoice`.name and item_code = '{0}'  
order by `tabPurchase Invoice`.creation desc limit 1) 
from `tabItem` where item_code = '{0}'; """.format(item), as_list=1)
		return item_data
