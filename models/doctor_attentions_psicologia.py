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

class doctor_psicologia(osv.osv):

	_name = "doctor.psicologia"
	_order = "date_attention desc"

	def cerrar_atencion(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'state': 'cerrada'}, context=context)

		
	_columns = {
		'patient_id': fields.many2one('doctor.patient', 'Paciente', ondelete='restrict', readonly=True),
		'patient_photo': fields.related('patient_id', 'photo', type="binary", relation="doctor.patient", readonly=True),
		'date_attention': fields.datetime('Fecha de atencion', required=True, readonly=True),
		'origin': fields.char('Documento origen', size=64,
							  help="Reference of the document that produced this attentiont.", readonly=True),
        'professional_id': fields.many2one('doctor.professional', 'Doctor', required=True, readonly=True),
        'speciality': fields.related('professional_id', 'speciality_id', type="many2one", relation="doctor.speciality",
                                     string='Speciality', required=True, store=True, readonly=True,
                                     states={'cerrada': [('readonly', True)]}),
		'professional_photo': fields.related('professional_id', 'photo', type="binary", relation="doctor.professional",
											 readonly=True, store=False),
		'age_attention': fields.integer('Edad actual', readonly=True),
		'age_unit': fields.selection([('1', u'Años'), ('2', 'Meses'), ('3', 'Dias'), ], 'Unidad de medida de la edad',
									 readonly=True),
		'state': fields.selection([('abierta', 'Abierta'), ('cerrada', 'Cerrada')], 'Estado', readonly=True, required=True, states={'cerrada': [('readonly', True)]}),
		'motivo_consulta':fields.text('Motivo de Consulta', states={'cerrada': [('readonly', True)]} ), 
		'descripcion_fisica': fields.text(u'Descripción física', states={'cerrada': [('readonly', True)]} ),
		'plantilla_descripcion_fisica_id': fields.many2one('doctor.attentions.recomendaciones', 'Plantillas', states={'cerrada': [('readonly', True)]}),
		'comportamiento_consulta': fields.text(u'Comportamiento en consulta', states={'cerrada': [('readonly', True)]} ),
		'plantilla_comportamiento_consulta_id': fields.many2one('doctor.attentions.recomendaciones', 'Plantillas', states={'cerrada': [('readonly', True)]}),
		'estrategia_evaluacion': fields.text(u'Estrategias de evaluación', states={'cerrada': [('readonly', True)]} ),
		'plantilla_estrategia_evaluacion_id': fields.many2one('doctor.attentions.recomendaciones', 'Plantillas', states={'cerrada': [('readonly', True)]}),
		'plan_intervencion': fields.text(u'Plan de intervención', states={'cerrada': [('readonly', True)]} ),
		'plantilla_plan_intervencion_id': fields.many2one('doctor.attentions.recomendaciones', 'Plantillas', states={'cerrada': [('readonly', True)]}),
		'area_ajuste_ids': fields.one2many('doctor.attention_area_ajuste', 'attentiont_id', 'Area de ajuste',
											 ondelete='restrict', states={'cerrada': [('readonly', True)]}),
		'diseases_ids': fields.one2many('doctor.attentions.diseases', 'attentiont_psicologia_id', 'Diseases', ondelete='restrict',
										states={'cerrada': [('readonly', True)]}),
		
	}

	def onchange_patient(self, cr, uid, ids, patient_id, context=None):
		values = {}
		if not patient_id:
			return values
		patient_data = self.pool.get('doctor.patient').browse(cr, uid, patient_id, context=context)
		photo_patient = patient_data.photo

		values.update({
			'patient_photo': photo_patient,
			'age_attention' : self.calcular_edad(patient_data.birth_date),
			'age_unit' : self.calcular_age_unit(patient_data.birth_date)
		})
		return {'value': values}

	def onchange_professional(self, cr, uid, ids, professional_id, context=None):

		values = {}
		if not professional_id:
			return values
		professional_data = self.pool.get('doctor.professional').browse(cr, uid, professional_id, context=context)
		professional_img = professional_data.photo
		if professional_data.speciality_id.id:
			professional_speciality = professional_data.speciality_id.id
			values.update({
				'speciality': professional_speciality,
			})

		values.update({
			'professional_photo': professional_img,
		})
		return {'value': values}



	def calcular_edad(self,fecha_nacimiento):
		current_date = datetime.today()
		st_birth_date = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
		re = current_date - st_birth_date
		dif_days = re.days
		age = dif_days
		age_unit = ''
		if age < 30:
			age_attention = age,
			age_unit = '3'

		elif age > 30 and age < 365:
			age = age / 30
			age = int(age)
			age_attention = age,
			age_unit = '2'

		elif age >= 365:
			age = int((current_date.year-st_birth_date.year-1) + (1 if (current_date.month, current_date.day) >= (st_birth_date.month, st_birth_date.day) else 0))
			age_attention = age,
			age_unit = '1'
		
		return age

	def calcular_age_unit(self,fecha_nacimiento):
		current_date = datetime.today()
		st_birth_date = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
		re = current_date - st_birth_date
		dif_days = re.days
		age = dif_days
		age_unit = ''
		if age < 30:
			age_unit = '3'
		elif age > 30 and age < 365:
			age_unit = '2'

		elif age >= 365:
			age_unit = '1'

		return age_unit


	def onchange_plantillas(self, cr, uid, ids, plantilla_id, campo, context=None):
		res={'value':{}}
		if plantilla_id:
			cuerpo = self.pool.get('doctor.attentions.recomendaciones').browse(cr,uid,plantilla_id,context=context).cuerpo
			res['value'][campo]=cuerpo
		else:
			res['value'][campo]=''
		_logger.info(res)
		return res		



	def default_get(self, cr, uid, fields, context=None):
		res = super(doctor_psicologia,self).default_get(cr, uid, fields, context=context)

		if context.get('active_model') == "doctor.patient":
			id_paciente = context.get('default_patient_id')
		else:
			id_paciente = context.get('patient_id')

		if id_paciente:    
			fecha_nacimiento = self.pool.get('doctor.patient').browse(cr,uid,id_paciente,context=context).birth_date
			res['age_attention'] = self.calcular_edad(fecha_nacimiento)
			res['age_unit'] = self.calcular_age_unit(fecha_nacimiento)

		#con esto cargams los items de revision por sistemas
		ids = self.pool.get('doctor.area_ajuste').search(cr,uid,[('active','=',True)],context=context)
		registros = []
		for i in self.pool.get('doctor.area_ajuste').browse(cr,uid,ids,context=context):
			registros.append((0,0,{'area_ajuste_id' : i.id,}))
		#fin carga item revision sistemas

		res['area_ajuste_ids'] = registros
		_logger.info(res)

		return res

	def write(self, cr, uid, ids, vals, context=None):
		
		attentions_past = super(doctor_psicologia,self).write(cr, uid, ids, vals, context)
		
		ids_attention_past = self.pool.get('doctor.attention_area_ajuste').search(cr, uid, [('attentiont_id', '=', ids), ('descripcion', '=', False)], context=context)
		self.pool.get('doctor.attention_area_ajuste').unlink(cr, uid, ids_attention_past, context)

		return attentions_past


	_defaults = {
		'date_attention': lambda *a: datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
		'state': 'abierta',
	}


doctor_psicologia()