# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import sprint
from . import technology

class task(models.Model):
    _name = 'manage.task'
    _description = 'manage.task'

    name = fields.Char(string="Nombre", required=True, help="Ingrese el nombre")
    description = fields.Text()
    creation_date = fields.Datetime()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    sprint = fields.Many2one("manage.sprint")
    technology = fields.Many2many("manage.technology")

