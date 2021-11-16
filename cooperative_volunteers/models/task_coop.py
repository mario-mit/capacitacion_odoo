# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name="cooperative.task"
    _description="Model to manage a task for a cooperative voluntaree"
    
    name=fields.Char(string="Name", required=True)
    description=fields.Char(string="Description")
    task_type=fields.Selection(string="Type", required=True, selection=[('easy','Easy'),('medium','Medium'),('complex','Complex')])
    initial_date=fields.Datetime(string="Start date", required=True)
    finish_date=fields.Datetime(string="Finish date", required=True)
    repeat=fields.Boolean(string="Repeat", reuired=True, default=False)
    frecuency=fields.Selection(string="Frecuency", selection=[('day','Day'),('month','Month'),('year','Year')])
    
