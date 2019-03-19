# -*- coding: utf-8 -*-
# Copyright (c) 2019, Hardik Gadesha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProductQuery(Document):
	pass

@frappe.whitelist(allow_guest=True)
def getProductQuery(item_code):
	item_data = frappe.db.sql("""select item_name, description,stock_uom, standard_rate,wholesale_rate,
(select valuation_rate
from `tabStock Ledger Entry` 
where item_code =  '{0}' and is_cancelled='No' 
order by posting_date desc, posting_time desc, 
name desc limit 1),
(select rate from `tabPurchase Invoice Item`,`tabPurchase Invoice` 
where `tabPurchase Invoice Item`.parent = `tabPurchase Invoice`.name and item_code = '{0}'  
order by `tabPurchase Invoice`.creation desc limit 1),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'SN - B'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'AH - B'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'MN - B'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'SZ - B'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'SH - B'),
(select sum(actual_qty) from `tabBin` where item_code =  '{0}' and (warehouse = 'SN - B' or warehouse = 'SZ - B' or warehouse = 'AH - B' or warehouse = 'MN - B' or warehouse = 'SH - B')),
(select ordered_qty from `tabBin` where item_code =  '{0}' order by name limit 1)
from `tabItem` where  item_code =  '{0}'; """.format(item_code), as_list=1)
	return item_data
