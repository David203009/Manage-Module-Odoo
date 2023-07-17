from odoo import fields,models

class sprint(models.Model):
    _name = "manage.sprint"
    _description = "manage.sprint"

    name = fields.Char()
    description = fields.Text()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    task = fields.One2many("manage.task", "sprint")