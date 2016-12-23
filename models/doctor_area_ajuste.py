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


class doctor_area_ajuste(osv.osv):


	_name = "doctor.area_ajuste"

	_columns = {
		'name' : fields.char('Nombre', required=True, size=60),
		'active': fields.boolean('activo'),
	}

	_defaults = {
		'active' : True,
	}


doctor_area_ajuste()



class doctor_attention_area_ajuste(osv.osv):

	_name = "doctor.attention_area_ajuste"

	_columns = {
		'attentiont_id': fields.many2one('doctor.psicologia', 'Attention'),
		'area_ajuste_id': fields.many2one('doctor.area_ajuste', 'Area de ajuste', required=True,
										   ondelete='restrict'),
		'descripcion': fields.char(u'Descripción'),
	}

doctor_attention_area_ajuste()