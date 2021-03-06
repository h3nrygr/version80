# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Consultoria YarosLab (<http://www.yaroslab.com>)
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

{
    "name" : "Perú Localización - Topónimos", 
    "version" : "1.0",
    "author" : "YarosLab SAC",
    "website": "http://www.yaroslab.com/",
    "category": "Localization",
    "description": " Agrega departamentos, provincias y distritos del Perú",
    "depends" : ["base", "sale"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        'partner_view.xml',
        'res_country_data.xml',
        'company_view.xml',
        'res_country_view.xml',        
        'security/ir.model.access.csv',
        ],
    'installable' : True,
    'active' : False,
}
