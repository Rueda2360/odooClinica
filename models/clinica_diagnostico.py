# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ClinicaDiagnostico(models.Model):
    _name = 'clinica.diagnostico'
    _description = 'Diagnóstico médico'

    idPaciente = fields.Many2one('clinica.paciente', string='Paciente', required=True)
    idMedico = fields.Many2one('clinica.medico', string='Médico', required=True)
    fecha_diagnostico = fields.Date('Fecha de diagnóstico', default=fields.Date.today(), required=True)
    diagnostico = fields.Text('Diagnóstico')

    nombrePaciente = fields.Char(related='idPaciente.nombre', string='Nombre del Paciente')
    apellidosPaciente = fields.Char(related='idPaciente.apellidos', string='Apellidos del Paciente')
    

    nombreMedico = fields.Char(related='idMedico.nombre', string='Nombre del Médico')
    apellidosMedico = fields.Char(related='idMedico.apellidos', string='Apellidos del Médico')

    
    _sql_constraints = [
        ('diagnosito_unico', 'UNIQUE(paciente_id, medico_id, fecha_diagnostico)', 'Ya existe un diagnóstico para este paciente y médico en esta fecha.'),
    ]