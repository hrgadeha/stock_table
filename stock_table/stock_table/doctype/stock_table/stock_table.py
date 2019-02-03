# -*- coding: utf-8 -*-
# Copyright (c) 2019, Hardik Gadesha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StockTable(Document):
	pass

@frappe.whitelist(allow_guest=True)
def getWarehouse(company):
	query="select name from `tabWarehouse` where is_group = 0 and company = '"+str(company)+"';"
	li=[]
	dic=frappe.db.sql(query, as_dict=True)
	for i in dic:
		name=i['name']
		li.append([name])
	return li

@frappe.whitelist(allow_guest=True)
def getStockBalance(item_code, warehouse):
	balance_qty = "select warehouse,qty_after_transaction from `tabStock Ledger Entry` where item_code=  '"+str(item_code)+"' and warehouse=  '"+str(warehouse)+"' and is_cancelled='No' order by posting_date desc, posting_time desc, name desc limit 1";
	li=[]
	dic=frappe.db.sql(balance_qty, as_dict=True)
	for i in dic:
		warehouse,qty_after_transaction=i['warehouse'],i['qty_after_transaction']
		li.append([warehouse,qty_after_transaction])
	return li if balance_qty else 0.0
