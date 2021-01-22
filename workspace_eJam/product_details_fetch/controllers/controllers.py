# -*- coding: utf-8 -*-
from odoo import http
import json
from odoo.http import Controller, Response, request, route
import pdb

class ProductDetailsFetch(http.Controller):
    @http.route('/product_details_fetch/product_id/<int:product_id>', type='json', auth='none',csrf=False,Website=True)
    def product_details(self, product_id,*post):
        # pdb.set_trace()
        prod_temp_obj = request.env['product.template']
        prod_prod_obj = request.env['product.product']
        stock_quant_obj = request.env['stock.quant']
        product_temp_id = prod_prod_obj.sudo().search([('id', '=', product_id)]).product_tmpl_id  
        product_poduct_models_ids = request.env['product.product'].sudo().search([('id', '=',product_id)])
        if not product_poduct_models_ids:
            return Response("No product found", status=412)
        Name = product_poduct_models_ids.name
        Sale_Price = product_poduct_models_ids.list_price
        Cost = product_poduct_models_ids.standard_price
        on_hand_qty = stock_quant_obj.sudo().search([('product_id', '=', product_id)])
        qty =0.0
        # Cost = '0.0'
        for s_id in on_hand_qty:
            if s_id.quantity >0:
                qty = qty + s_id.quantity
        categ_name = product_poduct_models_ids.categ_id.name
        return {
                    "Name": Name,
                    "Sale_Price": Sale_Price,
                    "Cost": Cost,
                    "on_hand_qty":qty,
                    "categ_name":categ_name,
                }
