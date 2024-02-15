# -*- coding: utf-8 -*-


from odoo import models, fields

class ClinicaMedico(models.Model):
    _name = 'clinica.paciente'
    _description = 'Médico en la clínica'

    nombre = fields.Char('Nombre')
    apellidos = fields.Char('Apellido')
    sintomas = fields.Text('Síntomas')