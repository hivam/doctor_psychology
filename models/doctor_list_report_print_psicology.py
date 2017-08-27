class doctor_list_report_print(osv.osv):

	_name= 'doctor.list_report_print_psicology'

	_columns = {
		'professional_id': fields.many2one('doctor.professional', 'Doctor'),
		'attentions_ids': fields.one2many('doctor.attentions', 'list_report_print_id', 'Attentions'),
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
		datas = {
			'ids': ids,
			'model': 'doctor.list_report_print',
			'form': data
			}
		_logger.info(datas)
		return {
			'type': 'ir.actions.report.xml',
			'report_name': 'doctor_attention_report_print',

		}

	#Funcion para cargar las ultimas atenciones
	def onchange_cargar_atenciones_print(self, cr, uid, ids, patient_id, professional_id, context=None):
		atenciones=''
		if patient_id and professional_id:
			atenciones = self.pool.get('doctor.attentions').search(cr, uid, [('patient_id', '=', patient_id), ('professional_id', '=', professional_id)])
			atenciones_id=[]
			if len(atenciones) > 4:
				for x in range(1, 4):
					_logger.info(atenciones[x])
					atenciones_id.append(atenciones[x])
				return {'value': {'attentions_ids': atenciones_id}}
			else:
				for x in range(len(atenciones)):
					atenciones_id.append(atenciones[x])
				return {'value': {'attentions_ids': atenciones_id}}
		return False

doctor_list_report_print()