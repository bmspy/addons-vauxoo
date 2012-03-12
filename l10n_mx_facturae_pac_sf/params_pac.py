# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#    Coded by: Isaac Lopez (isaac@vauxoo.com)
#    Financed by: http://www.sfsoluciones.com (aef@sfsoluciones.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from tools.translate import _
from osv import fields, osv
import pooler


class params_pac(osv.osv):
    _inherit = 'params.pac'
    
    def _get_method_type_selection(self, cr, uid, context=None):
        types = super(params_pac, self)._get_method_type_selection(cr, uid, context=context)
        types.extend([
            ('pac_sf_cancelar','PAC SF - Cancelar'),
            ('pac_sf_firmar','PAC SF - Firmar'),
        ])
        return types
    
    _columns = {
        'method_type': fields.selection(_get_method_type_selection, "Proceso a realizar", type='char', size=64, required=True),
    }
params_pac()

