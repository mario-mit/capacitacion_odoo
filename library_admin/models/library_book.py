# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name="library.book"
    _description="Model to manage a book from library"
    
    name=fields.Char(string="Name", required=True)
    authors=fields.Text(string="authors", required=True)
    editor=fields.Text(string="Editor", required=True)
    editorial=fields.Char(string="Editorial", required=True)
    year_edition=fields.Integer(string="Year", required=True)
    isbn=fields.Char(string="ISBN", required=True)
    gender=fields.Seleccion(string="Gender", required=True, selection=[('action','Action'),('drama','Drama'),('terror','Terror'),('science','Science'),('sports','Sports')])
    