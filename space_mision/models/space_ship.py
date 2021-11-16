# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Space_Ship(models.Model):
    _name="space.ship"
    _description="Model to manager a space ship"
    
    name=fields.Char(string="Name", required=True)
    width=fields.Float(string="Width",required=True)
    height=fields.Float(string="Height",required=True)
    length=fields.Float(string="Length",required=True)
    ship_type=fields.Selection(string="Type", required=True, selection=[('small','Small'),('medium','Medium'),('large','Large')])
    fuel_type=fields.Selection(string="Fuel", required=True, selection=[('solid','Solid'),('liquid','Liquid')])
    num_pasangers=fields.Integer(string="# Passangers", required=True)
    active=fields.Boolean(string="Active", required=True, default=True)
    