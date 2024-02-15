from odoo import models, fields

class ClinicaMedico(models.Model):
    _name = 'clinica.paciente'
    _description = 'Paciente de la clínica'

    nombre = fields.Char('Nombre')
    apellidos = fields.Char('Apellido')
    numero_colegiado = fields.Char('Número de Colegiado')
