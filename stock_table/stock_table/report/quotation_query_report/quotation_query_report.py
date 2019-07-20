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
	return [_("Item Name") + ":Data:180",_("Brand") + ":Data:80",_("UOM") + ":Data:80",
		_("Image") + ":Image:150",_("Payment Terms") + ":Data:180",
		_("Sales Price") + ":Currency:100",_("Valuation Rate") + ":Currency:100",_("Last Purchase Price") + ":Data:180",
		_("Market Price") + ":Currency:100",_("Price A 60 Days") + ":Currency:140",_("Price B 90 Days") + ":Currency:140",
		_("Cash Price") + ":Currency:100",_("Sell Off Price") + ":Currency:140",
		_("Last Quoted Price") + ":Currency:140",_("Last Sold Price") + ":Currency:140",
		_("Main Stock") + ":Float:100",_("Ahmadi Stock") + ":Float:100",_("Decor Stock") + ":Float:100",
		_("Shuwaikh Stock") + ":Float:100",_("Store Shuwaikh Stock") + ":Float:160"]

def get_data(filters):
	if filters.get("customer","item"):
		customer = filters.get("customer")
		item = filters.get("item")
		item_data = frappe.db.sql("""select item_name,brand,stock_uom,CONCAT("<img src=",image,">"),
		(select payment_terms from `tabCustomer` where customer_name = '{0}'),standard_rate,
		(select valuation_rate	from `tabStock Ledger Entry` where item_code =  '{1}' and is_cancelled='No' order by posting_date desc, posting_time desc, name desc limit 1),
		(select CONCAT(sitem.rate," ",si.currency) from `tabPurchase Invoice Item` sitem,`tabPurchase Invoice` si
                where sitem.parent = si.name and sitem.item_code = '{1}' order by si.creation desc limit 1),
		market_price,price_a_60_days,price_a_90_days,cash_price,sell_off_price,
		(select qitem.rate from `tabQuotation Item` qitem,`tabQuotation` qt
		where qitem.parent = qt.name and qitem.item_code = '{1}'  and qt.customer_name = '{0}'
		order by qt.creation desc limit 1),
		(select sitem.rate from `tabSales Invoice Item` sitem,`tabSales Invoice` si
		where sitem.parent = si.name and sitem.item_code = '{1}'  and si.customer = '{0}'
		order by si.creation desc limit 1),
		(select actual_qty from `tabBin` where item_code =  '{1}' and warehouse = 'Main SB - SB'),
		(select actual_qty from `tabBin` where item_code =  '{1}' and warehouse = 'Ahmadi S/R - SB'),
		(select actual_qty from `tabBin` where item_code =  '{1}' and warehouse = 'Decor - Shuwaikh - SB'),
		(select actual_qty from `tabBin` where item_code =  '{1}' and warehouse = 'Shuwaikh S/R - SB'),
		(select actual_qty from `tabBin` where item_code =  '{1}' and warehouse = 'Store - Shuwaikh - SB')
from `tabItem` where  item_code =  '{1}'; """.format(customer,item), as_list=1)
		return item_data
