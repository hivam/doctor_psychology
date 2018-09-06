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



	def _set_ref(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('ref', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'ref' : field_value})

	def _set_fecha_nacimiento(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('birth_date', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'birth_date' : field_value})


	def _set_primer_nombre(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('firstname', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'firstname' : field_value})


	def _set_segundo_nombre(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('middlename', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'middlename' : field_value})


	def _set_primer_apellido(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('lastname', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'lastname' : field_value})


	def _set_segundo_apellido(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('surname', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'surname' : field_value})

	def _set_tdoc(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('tdoc', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'tdoc' : field_value})

	def _set_sexo(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('sex', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'sex' : field_value})

	def _set_ocupacion(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('ocupacion_actual', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'ocupacion_actual' : field_value})

	def _set_direccion(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('street', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'street' : field_value})

	def _set_telefono(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('telefono', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'telefono' : field_value})


	def _set_nom_acom(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('nombre_acompaniante', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'nombre_acompaniante' : field_value})

	def _set_tel_acom(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('telefono_acompaniante', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'telefono_acompaniante' : field_value})


	def _set_nom_res(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('nombre_responsable', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'nombre_responsable' : field_value})


	def _set_blood_type(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('blood_type', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'blood_type' : field_value})




	def _set_rh(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('rh', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'rh' : field_value})




	def _set_tel_res(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('telefono_responsable', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'telefono_responsable' : field_value})


	def _set_creencias(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('creencias', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'creencias' : field_value})


	def _set_profesion(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('ocupacion_id', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'ocupacion_id' : field_value})

	def _set_insurer(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('insurer_prepagada_id', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'insurer_prepagada_id' : field_value})

	def _set_parentesco(self, cr, uid, ids, field_name, field_value, arg, context=None):
		field_value = field_value or None
		if field_value:
			for datos in self.browse(cr, uid, [ids], context=context):
				dato_cambio_id = self.pool.get('doctor.patient').search(cr, uid, [('id', '=', datos.patient_id.id), 
					('parentesco_id', '=', field_value)], context=context)
				if not dato_cambio_id:
					return self.pool.get('doctor.patient').write(cr, uid, [datos.patient_id.id], {'parentesco_id' : field_value})



	def _get_ref(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = datos.patient_id.ref
		return res

	def _get_edad_paciente(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = self.calcular_edad(datos.patient_id.birth_date)
		return res

	def _get_unidad_edad_paciente(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = self.calcular_age_unit(datos.patient_id.birth_date)
		return res

	def _get_fecha_nacimiento(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = datos.patient_id.birth_date
		return res

	def _get_primer_nombre(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = datos.patient_id.firstname
		return res

	def _get_segundo_nombre(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.middlename:
				res[datos.id] = datos.patient_id.middlename
		return res

	def _get_primer_apellido(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = datos.patient_id.lastname
		return res

	def _get_segundo_apellido(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.surname:
				res[datos.id] = datos.patient_id.surname
		return res

	def _get_tdoc(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = datos.patient_id.tdoc
		return res

	def _get_sexo(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = datos.patient_id.sex
		return res

	def _get_ocupacion(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.ocupacion_actual:
				res[datos.id] = datos.patient_id.ocupacion_actual
		return res


	def _get_direccion(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.street:
				res[datos.id] = datos.patient_id.street
		return res


	def _get_telefono(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.telefono:
				res[datos.id] = datos.patient_id.telefono
		return res


	def _get_nom_acom(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.nombre_acompaniante:
				res[datos.id] = datos.patient_id.nombre_acompaniante
		return res


	def _get_tel_acom(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.telefono_acompaniante:
				res[datos.id] = datos.patient_id.telefono_acompaniante
		return res


	def _get_nom_res(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.nombre_responsable:
				res[datos.id] = datos.patient_id.nombre_responsable
		return res

	def _get_tel_res(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.telefono_responsable:
				res[datos.id] = datos.patient_id.telefono_responsable
		return res

	def _get_creencias(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.creencias:
				res[datos.id] = datos.patient_id.creencias
		return res


	def _get_profesion(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.ocupacion_id:
				res[datos.id] = datos.patient_id.ocupacion_id.id
		return res

	def _get_insurer(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.insurer_prepagada_id:
				res[datos.id] = datos.patient_id.insurer_prepagada_id.id
		return res

	def _get_parentesco(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			if datos.patient_id.parentesco_id:
				res[datos.id] = datos.patient_id.parentesco_id.id
		return res


	def _get_blood_type(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			_logger.info("TIPO DE SANGRE")
			_logger.info(datos.patient_id.rh)
			res[datos.id] = datos.patient_id.blood_type
		return res



	def _get_rh(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = datos.patient_id.rh
		return res



	def  _get_adjuntos(self, cr, uid, ids, field_name, arg, context=None):

		res = {}
		for datos in self.browse(cr, uid, ids):
			modelo_buscar = self.pool.get('ir.attachment')
			adjuntos_id = modelo_buscar.search(cr, uid, [('res_id', '=', datos.patient_id)], context=context)

			if adjuntos_id:
				res[datos.id] = adjuntos_id
		return res	



	def load_attentions_diseases_ago(self, cr, uid, ids, field_name, arg, context=None):
		res = {}
		patient_id=None
		for datos in self.browse(cr, uid, ids):
			patient_id= datos.patient_id.id
		atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id)])	
		diseases_ago_ids = self.pool.get('doctor.attentions.diseases').search(cr, uid, [('attentiont_id', 'in', atenciones),])
		for datos in self.browse(cr, uid, ids):
			res[datos.id] = diseases_ago_ids

		return res

	_columns = {
		'patient_id': fields.many2one('doctor.patient', 'Paciente', ondelete='restrict', readonly=True),
		'patient_photo': fields.related('patient_id', 'photo', type="binary", relation="doctor.patient", readonly=True),
		'date_attention': fields.datetime('Fecha de atencion', required=True, readonly=True),
		'origin': fields.char('Documento origen', size=64,
							  help="Reference of the document that produced this attentiont.", readonly=True),
		'professional_id': fields.many2one('doctor.professional', 'Doctor', required=True, readonly=True),
		'speciality': fields.related('professional_id', 'speciality_id', type="many2one", relation="doctor.speciality",
									 string='Especialidad', required=True, store=True, readonly=True,
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

		'paciente_identificacion': fields.function(_get_ref, fnct_inv=_set_ref , type="char", store= False, 
								string=u'Identificación', required=True), 
		'paciente_edad_atencion': fields.function(_get_edad_paciente, type='integer', store=False, required=True, readonly=True, string='Edad Actual',),
		'paciente_unidad_edad': fields.function(_get_unidad_edad_paciente, type='selection', selection=[('1', u'Años'), ('2', 'Meses'), ('3', 'Dias'),], string='Unidad medida edad',
									store=False, required=True, readonly=True),
		'paciente_birth_date': fields.function(_get_fecha_nacimiento, fnct_inv=_set_fecha_nacimiento, type='date', string=u'Fecha cumpleaños', required=True, store=False),
		
		'paciente_primer_nombre': fields.function(_get_primer_nombre, fnct_inv=_set_primer_nombre, type="char", store= False, 
								string=u'Primer Nombre', required=True), 
		'paciente_segundo_nombre': fields.function(_get_segundo_nombre, fnct_inv=_set_segundo_nombre, type="char", store= False, 
								string=u'Segundo Nombre',), 
		'paciente_primer_apellido': fields.function(_get_primer_apellido, fnct_inv=_set_primer_apellido, type="char", store= False, 
								string=u'Primer Apellido', required=True), 
		'paciente_segundo_apellido': fields.function(_get_segundo_apellido, fnct_inv=_set_segundo_apellido, type="char", store= False, 
								string=u'Segundo Apellido',),
		'paciente_tdoc': fields.function(_get_tdoc, fnct_inv=_set_tdoc, type='selection', selection=[('11','Registro civil'), ('12','Tarjeta de identidad'),
								  ('13',u'Cédula de ciudadanía'), ('21',u'Cédula de extranjería'), ('41','Pasaporte'),
								  ('NU',u'Número único de identificación'), ('AS',u'Adulto sin identificación'), ('MS',u'Menor sin identificación')],
								  string='Tipo Documento', store=False, required=True, readonly=True),		
		'paciente_sexo': fields.function(_get_sexo,fnct_inv=_set_sexo, type='selection', selection=[('m', 'Masculino'), ('f', 'Femenino'),], string='Sexo',
									store=False, required=True, readonly=True),

		'paciente_ocupacion_actual': fields.function(_get_ocupacion, fnct_inv=_set_ocupacion , type="char", store= False, 
								string=u'Ocupacion'), 
		'paciente_street': fields.function(_get_direccion, fnct_inv=_set_direccion , type="char", store= False, 
								string=u'Dirección'), 
		'paciente_telefono': fields.function(_get_telefono, fnct_inv=_set_telefono , type="char", store= False, 
								string=u'telefono'), 
		'paciente_nombre_acompaniante': fields.function(_get_nom_acom, fnct_inv=_set_nom_acom , type="char", store= False, 
								string=u'Nombre Acompañante'), 
		'paciente_telefono_acompaniante': fields.function(_get_tel_acom, fnct_inv=_set_tel_acom , type="char", store= False, 
								string=u'Teléfono Acompañante'), 
		'paciente_nombre_responsable': fields.function(_get_nom_res, fnct_inv=_set_nom_res , type="char", store= False, 
								string=u'Nombre responsable'), 
		'paciente_telefono_responsable': fields.function(_get_tel_res, fnct_inv=_set_tel_res , type="char", store= False, 
								string=u'Telefono responsable'), 
		'paciente_ocupacion_id': fields.function(_get_profesion, fnct_inv=_set_profesion , type="many2one", store= False, 
								string=u'Profesión', relation='doctor.patient.ocupacion'), 
		'paciente_insurer_prepagada_id': fields.function(_get_insurer, fnct_inv=_set_insurer , type="many2one", store= False, 
								string=u'Aseguradora', relation='doctor.insurer'),
		'paciente_parentesco_id': fields.function(_get_parentesco, fnct_inv=_set_parentesco , type="many2one", store= False, 
								string=u'Parentesco', relation='doctor.patient.parentesco'),

		'paciente_blood_type': fields.function(_get_blood_type,fnct_inv=_set_blood_type, type='selection', selection=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string='Tipo Sangre',
									store=False),

		'paciente_rh': fields.function(_get_rh,fnct_inv=_set_rh, type='selection', selection=[('+', '+'), ('-', '-'), ], string='Rh',
									store=False),

		'paciente_creencias': fields.function(_get_creencias, fnct_inv=_set_creencias , type="char", store= False, 
								string=u'Creencias'), 


		'adjuntos_paciente_psico_ids': fields.function(_get_adjuntos, type="one2many", store= False, 
								string=u'Adjuntos', relation='ir.attachment',states={'closed': [('readonly', True)]}),


		'diseases_ago_ids': fields.function(load_attentions_diseases_ago, relation="doctor.attentions.diseases", type="one2many", store=False, readonly=True, method=True, string=u"Diagnósticos Anteriores"),
		
		'certificados_ids': fields.one2many('doctor.attentions.certificado', 'attentiont_psicologia_id', u'Certificados',states={'closed': [('readonly', True)]}),

		'img_familiograma': fields.binary('Familiograma', states={'cerrada': [('readonly', True)]}),

		'paciente_otros': fields.text('Otros'),
		'plantilla_paciente_otros': fields.many2one('doctor.attentions.recomendaciones', 'Plantillas'),
		'list_report_print_spicologia_id': fields.many2one('doctor.list_report', 'List Report'),

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

	def onchange_edad(self, cr, uid, ids, birth_date, context=None):
		res={'value':{}}
		if birth_date:
			res['value']['paciente_edad_atencion']= self.calcular_edad(birth_date)
			res['value']['paciente_unidad_edad']=self.calcular_age_unit(birth_date)
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

		
		professional_id = self.pool.get('doctor.professional').search(cr, uid,[('user_id', '=', uid)], context=context)
		for especialidad in self.pool.get('doctor.professional').browse(cr, uid, professional_id, context=context):
			especialidad_id = especialidad.speciality_id.id
		
		if professional_id:
			res['professional_id'] = professional_id[0]
			res['speciality'] = especialidad_id
		


		if id_paciente:
			registro = []
			arreglo_ago=[]
			atenciones = self.search(cr, uid, [('patient_id', '=', id_paciente)])	
			_logger.info(atenciones)

			img_familiograma_id = self.search(cr, uid, [('patient_id', '=', id_paciente)], order='id asc', context=context)
			if img_familiograma_id:
				_logger.info(img_familiograma_id)
				for familiograma in self.browse(cr, uid, img_familiograma_id, context=context):
					if familiograma.img_familiograma:
						res['img_familiograma'] = familiograma.img_familiograma


			diseases_ago_ids = self.pool.get('doctor.attentions.diseases').search(cr, uid, [('attentiont_psicologia_id', 'in', atenciones)])
			

			for otros_paciente in self.browse(cr, uid, atenciones, context=context):

				if otros_paciente.paciente_otros:

					res['paciente_otros'] = otros_paciente.paciente_otros + '\n'


			for i in self.pool.get('doctor.attentions.diseases').browse(cr,uid,diseases_ago_ids,context=context):
				arreglo_ago.append((0,0,{'diseases_id' : i.diseases_id.id , 'status' : i.status, 'diseases_type': i.diseases_type}))

			for datos_paciente in self.pool.get('doctor.patient').browse(cr, uid, [id_paciente], context=context):

				ref = datos_paciente.ref
				tdoc = datos_paciente.tdoc

				res['paciente_tdoc'] = datos_paciente.tdoc
				res['paciente_identificacion'] = datos_paciente.ref
				res['paciente_primer_nombre'] = datos_paciente.firstname
				res['paciente_primer_apellido'] = datos_paciente.lastname
				res['paciente_sexo'] = datos_paciente.sex
				res['paciente_birth_date'] = datos_paciente.birth_date
				res['paciente_edad_atencion'] = self.calcular_edad(datos_paciente.birth_date)
				res['paciente_unidad_edad'] = self.calcular_age_unit(datos_paciente.birth_date)

				if datos_paciente.middlename:
					res['paciente_segundo_nombre'] = datos_paciente.middlename
				if datos_paciente.surname:
					res['paciente_segundo_apellido'] = datos_paciente.surname
				if datos_paciente.ocupacion_actual:
					res['paciente_ocupacion_actual'] = datos_paciente.ocupacion_actual
				if datos_paciente.ocupacion_id:
					res['paciente_ocupacion_id'] = datos_paciente.ocupacion_id.id
				if datos_paciente.street:
					res['paciente_street'] = datos_paciente.street
				if datos_paciente.telefono:
					res['paciente_telefono'] = datos_paciente.telefono
				if datos_paciente.nombre_acompaniante:
					res['paciente_nombre_acompaniante'] = datos_paciente.nombre_acompaniante
				if datos_paciente.telefono_acompaniante:
					res['paciente_telefono_acompaniante'] = datos_paciente.telefono_acompaniante
				if datos_paciente.nombre_responsable:
					res['paciente_nombre_responsable'] = datos_paciente.nombre_responsable
				if datos_paciente.telefono_responsable:
					res['paciente_telefono_responsable'] = datos_paciente.telefono_responsable
				if datos_paciente.parentesco_id:
					res['paciente_parentesco_id'] = datos_paciente.parentesco_id.id
				if datos_paciente.insurer_prepagada_id:
					res['paciente_insurer_prepagada_id'] = datos_paciente.insurer_prepagada_id.id
				if datos_paciente.creencias:
					res['paciente_creencias'] = datos_paciente.creencias
				if datos_paciente.rh:
					res['paciente_rh'] = datos_paciente.rh
				if datos_paciente.blood_type:
					res['paciente_blood_type'] = datos_paciente.blood_type

			modelo_buscar = self.pool.get('ir.attachment')

			adjuntos_id = modelo_buscar.search(cr, uid, [('res_id', '=', id_paciente)], context=context)

			if adjuntos_id:
				
				for datos in modelo_buscar.browse(cr, uid, adjuntos_id, context=context):
					registro.append((0,0,{'name' : datos.name, 'datas' : datos.datas})) 

			res['ref'] = ref
			res['tdoc'] = self.pool.get('doctor.doctor').tipo_documento(tdoc)
			res['diseases_ago_ids'] = arreglo_ago

		if registro:		
			res['adjuntos_paciente_ids'] = registro
				

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

	def button_imprimir_informes(self, cr, uid, ids, context=None):
		data_obj = self.pool.get('ir.model.data')
		result = data_obj._get_id(cr, uid, 'l10n_co_doctor', 'view_doctor_list_report_form')
		view_id = data_obj.browse(cr, uid, result).res_id

		profesional=''
		patient=''
		for x in self.browse(cr,uid,ids):
			patient= x.patient_id.id
			profesional= x.professional_id.id

		context['default_patient_id']= patient
		context['default_professional_id']= profesional
		context['default_ultimas_citas'] = False

		return {
			'type': 'ir.actions.act_window',
			'name': 'Ver Historia Clínica Completa',
			'view_type': 'form',
			'view_mode': 'form',
			'res_id': False,
			'res_model': 'doctor.list_report',
			'context': context or None,
			'view_id': [view_id] or False,
			'nodestroy': False,
			'target': 'new'
		}



	def button_imprimir_ultimas_hc(self, cr, uid, ids, context=None):


		data_obj = self.pool.get('ir.model.data')
		result = data_obj._get_id(cr, uid, 'l10n_co_doctor', 'view_doctor_list_report_form')
		view_id = data_obj.browse(cr, uid, result).res_id


		profesional=''
		patient=''
		for x in self.browse(cr,uid,ids):
			patient= x.patient_id.id
			profesional= x.professional_id.id

		context['default_patient_id']= patient
		context['default_professional_id']= profesional
		context['default_ultimas_citas'] = True

		return {
			'type': 'ir.actions.act_window',
			'name': 'Ver Historia Clínica Completa',
			'view_type': 'form',
			'view_mode': 'form',
			'res_id': False,
			'res_model': 'doctor.list_report',
			'context': context or None,
			'view_id': [view_id] or False,
			'nodestroy': False,
			'target': 'new'
		}

	_defaults = {
		'date_attention': lambda *a: datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
		'state': 'abierta',
	}


doctor_psicologia()