class doctor_list_report(osv.osv):

	_name= 'doctor.list_report_psicology'


	_columns = {
		'professional_id': fields.many2one('doctor.professional', 'Doctor'),
		'attentions_ids': fields.one2many('doctor.attentions', 'list_report_id', 'Attentions'),
		'patient_id': fields.many2one('doctor.patient', 'Paciente', required=True),
		'fecha_inicio':fields.datetime('Inicio Atención'),
		'fecha_fin':fields.datetime('Fin Atención'),
		'especialidad_id':fields.many2one('doctor.speciality', 'Especialidad'),

	}

	_defaults = {
		'patient_id' : lambda self, cr, uid, context: context.get('default_patient_id', False),
		'professional_id' : lambda self, cr, uid, context: context.get('default_professional_id', False),
		#'fecha_fin' : lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	}	

	#Funcion para cargar los seguimientos paraclinicos de acuerdo a una relacion
	def onchange_cargar_atenciones_doctor(self, cr, uid, ids, patient_id, professional_id, date_begin, date_end, context=None):
		atenciones=''
		arreglo= [patient_id, professional_id, date_begin, date_end]
		if patient_id and professional_id:
			if (arreglo[0] != False) and (arreglo[1] != False) and (arreglo[2] == False) and (arreglo[3] == False):
				_logger.info('Caso doctor')
				atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id), ('professional_id', '=', professional_id)])
				return {'value': {'attentions_ids': atenciones, 'especialidad_id': None}}
		return False

	#Funcion para cargar los seguimientos paraclinicos de acuerdo a una relacion
	def onchange_cargar_atenciones_especialidad(self, cr, uid, ids, patient_id, especialidad_id, date_begin, date_end, context=None):
		atenciones=''
		arreglo= [patient_id, especialidad_id, date_begin, date_end]
		if patient_id and especialidad_id:
			_logger.info('especialidad')
			if (arreglo[0] != False) and (arreglo[1] != False) and (arreglo[2] == False) and (arreglo[2] == False):
				_logger.info('Caso especialidad')
				atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id), ('speciality', '=', especialidad_id)])
				return {'value': {'attentions_ids': atenciones, 'professional_id': None}}
		return False

	#Funcion para cargar los seguimientos paraclinicos de acuerdo a una relacion
	def onchange_cargar_atenciones_fecha_inicio(self, cr, uid, ids, patient_id, especialidad_id, date_begin, date_end, context=None):
		atenciones=''
		arreglo= [patient_id, especialidad_id, date_begin, date_end]
		if patient_id and especialidad_id:
			_logger.info('especialidad')
			if (arreglo[0] != False) and (arreglo[1] != False) and (arreglo[2] == False) and (arreglo[2] == False):
				_logger.info('Caso especialidad')
				atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id), ('speciality', '=', especialidad_id)])
				return {'value': {'attentions_ids': atenciones, 'professional_id': None}}
		return False

	#Funcion para cargar los seguimientos paraclinicos de acuerdo a una relacion
	def onchange_cargar_atenciones_fecha_fin(self, cr, uid, ids, patient_id, especialidad_id, date_begin, date_end, context=None):
		atenciones=''
		arreglo= [patient_id, especialidad_id, date_begin, date_end]
		if patient_id and especialidad_id:
			_logger.info('especialidad')
			if (arreglo[0] != False) and (arreglo[1] != False) and (arreglo[2] == False) and (arreglo[2] == False):
				_logger.info('Caso especialidad')
				atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id), ('speciality', '=', especialidad_id)])
				return {'value': {'attentions_ids': atenciones, 'professional_id': None}}
		return False

	#Funcion para cargar los seguimientos paraclinicos de acuerdo a una relacion
	def onchange_cargar_atenciones(self, cr, uid, ids, patient_id, professional_id, especialidad_id, date_begin, date_end, context=None):


		atenciones=''
		doctor=''
		paciente=''
		especialidad=''
		fecha_incio=''
		fecha_fin=''

		is_selected_professional=False
		is_selected_speciality= False

		arreglo= [patient_id, professional_id, especialidad_id, date_begin, date_end]

		if (arreglo[0] != False) and (arreglo[1] == False) and (arreglo[2] == False) and (arreglo[3] == False) and (arreglo[4] == False):
			_logger.info('Caso 1')
			atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id)])	
			return {'value': {'attentions_ids': atenciones}}

		if (arreglo[0] != False) and (arreglo[1] != False) and (arreglo[2] == False) and (arreglo[3] == False) and (arreglo[4] == False):
			_logger.info('Caso 2')
			atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id), ('professional_id', '=', professional_id)])	
			return {'value': {'attentions_ids': atenciones}}

		#if (arreglo[0] != False) and (arreglo[1] != False) and (arreglo[2] != False) and (arreglo[3] == False) and (arreglo[4] == False):
		#	_logger.info('Caso 3')
		#	atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id), ('professional_id', '=', professional_id)])
		#	return {'value': {'attentions_ids': atenciones, 'especialidad_id': ''}}


		if (arreglo[0] != False) and (arreglo[1] == False) and (arreglo[2] != False) and (arreglo[3] == False) and (arreglo[4] == False):
			_logger.info('Caso 4')
			atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id), ('speciality', '=', especialidad_id)])
			return {'value': {'attentions_ids': atenciones}}

		if (arreglo[0] != False) and (arreglo[1] != False) and (arreglo[2] == False) and (arreglo[3] != False) and (arreglo[4] != False):
			_logger.info('Caso 5')
			atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('date_attention', '>=', str(date_begin)),('date_attention', '<=', str(date_end))])
			_logger.info(atenciones)
			return {'value': {'attentions_ids': atenciones}}

		if (arreglo[0] != False) and (arreglo[1] == False) and (arreglo[2] == False) and (arreglo[3] != False) and (arreglo[4] != False):
			_logger.info('Caso 6')
			atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id), ('date_attention', '>=', str(date_begin)),('date_attention', '<=', str(date_end))])
			_logger.info(atenciones)
			return {'value': {'attentions_ids': atenciones}}			

		if (arreglo[3] == False) and (arreglo[4] != False):
			raise osv.except_osv(_('Error al cargar las Atenciones!'),_('Para cargar las Atenciones por fechas \n Debe seleccionar una fecha incial'))
		

			



		_logger.info('Atenciones')
		_logger.info(atenciones)
		return True

	

	def button_imprimir_algunos_informes(self, cr, uid, ids, context=None):
		_logger.info(ids)
		_logger.info(context)
		return self.export_report_print(cr, uid, ids, 'doctor_attention')
	def onchange_imprimir_algunos_informes(self, cr, uid, ids, report_uno, report_dos, context=None):
		_logger.info(report_uno)
		_logger.info(report_dos)
		_logger.info('imprimir')
		return self.export_report_print(uid, ids, 'doctor_attention')
	

	def export_report_print(self, cr, uid, ids, name_report, context=None):
		if context is None:
			context = {}
		data = self.read(cr, uid, ids)[0]
		_logger.info('entro')
		_logger.info(data)
		datas = {
			'ids': ids,
			'model': 'doctor.list_report',
			'form': data
			}
		_logger.info(datas)
		return {
			'type': 'ir.actions.report.xml',
			'report_name': 'doctor_attention_report',

		}
	


doctor_list_report()