// Copyright (c) 2019, Hardik Gadesha and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quotation Query', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Quotation Query", {
  item_code: function(frm) {
	cur_frm.refresh();
	cur_frm.refresh_fields();

	if(frm.doc.item_code){

    frappe.call({
    "method": "stock_table.stock_table.doctype.quotation_query.quotation_query.getQuotationQuery",
args: {
doctype: "Quotation Query",
item_code: frm.doc.item_code,
customer: frm.doc.customer
},
callback:function(r){
	console.log(r)
	var len=r.message.length;
	for (var i=0;i<len;i++){
		frm.set_value("item_name",r.message[i][0]);
                frm.set_value("brand",r.message[i][1]);
                frm.set_value("uom",r.message[i][2]);
		frm.set_value("payment_terms",r.message[i][3]);
                frm.set_value("sales_price",r.message[i][4]);
                frm.set_value("valuation_rate",r.message[i][5]);
                frm.set_value("last_purchase_price",r.message[i][6]);
                frm.set_value("market_price",r.message[i][7]);
                frm.set_value("price_a_60_days",r.message[i][8]);
                frm.set_value("price_b_90_days",r.message[i][9]);
                frm.set_value("cash_price",r.message[i][10]);
                frm.set_value("sell_off_price",r.message[i][11]);
                frm.set_value("last_quoted_price",r.message[i][12]);
                frm.set_value("last_sold_price",r.message[i][13]);
                frm.set_value("ahmadi_sr_stock",r.message[i][14]);
		frm.set_value("decor_shuwaikh_stock",r.message[i][15]);
		frm.set_value("main_sb_stock",r.message[i][16]);
		frm.set_value("shuwaikh_sr_stock",r.message[i][17]);
		frm.set_value("store_shuwaikh_stock",r.message[i][18]);
		frm.set_value("total_stock",r.message[i][19]);
		frm.set_value("stock_in_transit",r.message[i][20]);
	}
		cur_frm.refresh();
	}
    });
}
}
});

