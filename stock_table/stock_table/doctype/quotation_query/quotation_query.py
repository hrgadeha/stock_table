# -*- coding: utf-8 -*-
# Copyright (c) 2019, Hardik Gadesha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QuotationQuery(Document):
	pass

@frappe.whitelist(allow_guest=True)
def getQuotationQuery(item_code,customer):
	item_data = frappe.db.sql("""select item_name, brand,stock_uom,(select payment_terms from `tabCustomer` where customer_name = '{1}'),standard_rate,
(select valuation_rate
from `tabStock Ledger Entry`
where item_code =  '{0}' and is_cancelled='No'
order by posting_date desc, posting_time desc,
name desc limit 1),
(select CONCAT(sitem.rate," ",si.currency) from `tabPurchase Invoice Item` sitem,`tabPurchase Invoice` si
where sitem.parent = si.name and sitem.item_code = '{0}' order by si.creation desc limit 1),
market_price,price_a_60_days,price_a_90_days,cash_price,sell_off_price,
(select qitem.rate from `tabQuotation Item` qitem,`tabQuotation` qt
where qitem.parent = qt.name and qitem.item_code = '{0}'  and qt.customer_name = '{1}' order by qt.creation desc limit 1),
(select sitem.rate from `tabSales Invoice Item` sitem,`tabSales Invoice` si
where sitem.parent = si.name and sitem.item_code = '{0}'  and si.customer = '{1}' order by si.creation desc limit 1),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'Ahmadi S/R - SB'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'Decor - Shuwaikh - SB'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'Main SB - SB'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'Shuwaikh S/R - SB'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'Store - Shuwaikh - SB'),
(select sum(actual_qty) from `tabBin` where item_code =  '{0}' and (warehouse = 'Ahmadi S/R - SB' or warehouse = 'Decor - Shuwaikh - SB' or warehouse = 'Main SB - SB' or warehouse = 'Shuwaikh S/R - SB' or warehouse = 'Store - Shuwaikh - SB')),
(select ordered_qty from `tabBin` where item_code =  '{0}' and ordered_qty != 0 order by name limit 1)
from `tabItem` where  item_code =  '{0}'; """.format(item_code,customer), as_list=1)
	return item_data
