# -*- coding: utf-8 -*-


from odoo import models, fields

class ClinicaPaciente(models.Model):
    _name = 'clinica.paciente'
    _description = 'Paciente de la clínica'

    nombre = fields.Char('Nombre')
    apellidos = fields.Char('Apellido')
    sintomas = fields.Text('Síntomas')