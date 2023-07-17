from odoo import fields,models
from . import task

class technology(models.Model):
    _name = "manage.technology"
    _description = "manage.technology"

    name = fields.Char()
    description = fields.Text()
    photo = fields.Image(max_width=200, max_heigth=200)
    task = fields.Many2many("manage.task")