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
	return [_("Item Code") + ":Data:180",_("Item Name") + ":Data:180",_("Discription") + ":Data:180",_("Sales Price") + ":Currency:100",_("Wholesale Price") + ":Currency:100",_("Last Sale Price") + ":Currency:100",_("Last Purchase Price") + ":Currency:100",_("SN Stock") + ":Float:100",_("AH Stock") + ":Float:100",_("MN Stock") + ":Float:100",_("SZ Stock") + ":Float:100",_("SH Stock") + ":Float:100"]

def get_data(filters):
	if filters.get("item"):
		item = filters.get("item")	
		item_data = frappe.db.sql("""select item_code, item_name, description, standard_rate, wholesale_rate , 
(select rate from `tabSales Invoice Item`,`tabSales Invoice` 
where `tabSales Invoice Item`.parent = `tabSales Invoice`.name and item_code = '{0}'  
order by `tabSales Invoice`.creation desc limit 1) AS 'Last Sale price',
(select rate from `tabPurchase Invoice Item`,`tabPurchase Invoice` 
where `tabPurchase Invoice Item`.parent = `tabPurchase Invoice`.name and item_code = '{0}'  
order by `tabPurchase Invoice`.creation desc limit 1),
(select qty_after_transaction 
from `tabStock Ledger Entry` 
where item_code =  '{0}' and warehouse = 'SN - B' and is_cancelled='No' 
order by posting_date desc, posting_time desc, 
name desc limit 1),
(select qty_after_transaction 
from `tabStock Ledger Entry` 
where item_code =  '{0}' and warehouse = 'AH - B' and is_cancelled='No' 
order by posting_date desc, posting_time desc, 
name desc limit 1),
(select qty_after_transaction 
from `tabStock Ledger Entry` 
where item_code =  '{0}' and warehouse = 'MN - B' and is_cancelled='No' 
order by posting_date desc, posting_time desc, 
name desc limit 1),
(select qty_after_transaction 
from `tabStock Ledger Entry` 
where item_code =  '{0}' and warehouse = 'SZ - B' and is_cancelled='No' 
order by posting_date desc, posting_time desc, 
name desc limit 1),
(select qty_after_transaction 
from `tabStock Ledger Entry` 
where item_code =  '{0}' and warehouse = 'SH - B' and is_cancelled='No' 
order by posting_date desc, posting_time desc, 
name desc limit 1)
from `tabItem` where  item_code =  '{0}';; """.format(item), as_list=1)
		return item_data
