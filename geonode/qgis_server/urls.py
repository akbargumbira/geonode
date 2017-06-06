# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import patterns, url

from geonode.qgis_server.views import (
    download_zip,
    tile,
    tile_404,
    legend,
    qgis_server_request,
    qgis_server_pdf,
    qgis_server_map_print,
    geotiff,
    ascii
)


urlpatterns = patterns(

    # Specific for a QGIS Layer
    '',
    url(
        r'^download-zip/'
        r'(?P<layername>[\w]*)'
        r'[\?]?'
        r'(?:&access_token=(?P<access_token>[\w]*))?$',
        download_zip,
        name='qgis-server-download-zip'
    ),
    url(
        r'^tiles/'
        r'(?P<layername>[^/]*)/'
        r'(?P<z>[0-9]*)/'
        r'(?P<x>[0-9]*)/'
        r'(?P<y>[0-9]*).png$',
        tile,
        name='qgis-server-tile'
    ),
    url(
        r'^tiles/'
        r'(?P<layername>[^/]*)/\{z\}/\{x\}/\{y\}.png',
        tile_404,
        name='qgis-server-tile'
    ),
    url(
        r'^geotiff/'
        r'(?P<layername>[\w]*)'
        r'[\?]?'
        r'(?:&access_token=(?P<access_token>[\w]*))?$',
        geotiff,
        name='qgis-server-geotiff'
    ),
    url(
        r'^ascii/'
        r'(?P<layername>[\w]*)'
        r'[\?]?'
        r'(?:&access_token=(?P<access_token>[\w]*))?$',
        ascii,
        name='qgis-server-ascii'
    ),
    url(
        r'^legend/(?P<layername>[\w]*)'
        r'(?:/(?P<layertitle>[\w]*))?'
        r'[\?]?'
        r'(?:&access_token=(?P<access_token>[\w]*))?$',
        legend,
        name='qgis-server-legend'
    ),

    # Generic for OGC
    # WMS entry point, this URL is not specific to WMS, you should remove it ?
    url(
        r'^wms/$',
        qgis_server_request,
        name='qgis-server-request'
    ),
    url(
        r'^ogc/$',
        qgis_server_request,
        name='qgis-server-request'
    ),

    # Generic for the app
    url(
        r'^pdf/info\.json$',
        qgis_server_pdf,
        name='qgis-server-pdf'
    ),
    url(
        r'^map/print$',
        qgis_server_map_print,
        name='qgis-server-map-print'
    ),
)