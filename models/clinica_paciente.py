# -*- coding: utf-8 -*-


from odoo import models, fields, api

class ClinicaPaciente(models.Model):
    _name = 'clinica.paciente'
    _description = 'Paciente de la clínica'
    _rec_name = 'nombreCompleto'

    nombre = fields.Char('Nombre')
    apellidos = fields.Char('Apellido')
    sintomas = fields.Text('Síntomas')
    
    #idDiagnostico = fields.One2many('clinica.diagnostico', 'idPaciente', string='Diagnósticos')

    nombreCompleto = fields.Char('Nombre Completo', compute='_compute_nombre_completo', store=True)

    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombreCompleto = f"{record.nombre} {record.apellidos}"