# -*- coding: utf-8 -*-
##############################################################################
#
#	OpenERP, Open Source Management Solution
#	Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU Affero General Public License as
#	published by the Free Software Foundation, either version 3 of the
#	License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU Affero General Public License for more details.
#
#	You should have received a copy of the GNU Affero General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import logging
_logger = logging.getLogger(__name__)
from openerp.osv import fields, osv
from openerp.tools.translate import _
import time
from datetime import date, datetime, timedelta
from lxml import etree


class doctor_report_print_last(osv.osv):

	_name= 'doctor.report_print_last'

	_columns = {
		'professional_id': fields.many2one('doctor.professional', 'Doctor'),
		'attentions_psychology_ids': fields.one2many('doctor.psicologia', 'list_report_print_spicologia_id', 'Attentions'),
		'patient_id': fields.many2one('doctor.patient', 'Paciente', required=True),
		'especialidad_id':fields.many2one('doctor.speciality', 'Especialidad'),
	}

	_defaults = {
		'patient_id' : lambda self, cr, uid, context: context.get('default_patient_id', False),
		'professional_id' : lambda self, cr, uid, context: context.get('default_professional_id', False),
	}	

	def button_print_attention(self, cr, uid, ids, context=None):
		if context is None:
			context = {}
		data = self.read(cr, uid, ids)[0]
		_logger.info('entro')
		_logger.info(data)
		return {
				'type': 'ir.actions.report.xml',
				'report_name': 'doctor_attention_psicologia_report'
				}		

	#Funcion para cargar las ultimas atenciones
	def onchange_cargar_atenciones_print(self, cr, uid, ids, patient_id, professional_id, context=None):
		atenciones=''
		if patient_id and professional_id:

			id_especialidad= self.pool.get('doctor.professional').browse(cr, uid, professional_id ).speciality_id.name

			atenciones = self.pool.get('doctor.psicologia').search(cr, uid, [('patient_id', '=', patient_id), ('professional_id', '=', professional_id)])
			atenciones_id=[]
			if len(atenciones) > 4:
				for x in range(1, 4):
					_logger.info(atenciones[x])
					atenciones_id.append(atenciones[x])
				return {'value': {'attentions_psychology_ids': atenciones_id}}
			else:
				for x in range(len(atenciones)):
					atenciones_id.append(atenciones[x])
				return {'value': {'attentions_psychology_ids': atenciones_id}}
				
doctor_report_print_last()