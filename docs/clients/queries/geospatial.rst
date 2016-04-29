==========
Geospatial
==========


Get intersecting
================

Get the documents where the given geometry object intersects with the specified
geospatial index.

.. container:: example python

    .. code-block:: python

        Query('movies').get_intersecting({
            'type': 'Polygon',
            'coordinates': [
                [
                    [-119.92675781249999, 36.82357691815722],
                    [-119.7509765625, 36.6739263393281],
                    [-119.57382202148439, 36.80598611937673],
                    [-119.73724365234375, 36.914764288955936],
                    [-119.92675781249999, 36.82357691815722]
                ]
            ]
      }, index='location')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').getIntersecting({
            'type': 'Polygon',
            'coordinates': [
                [
                    [-119.92675781249999, 36.82357691815722],
                    [-119.7509765625, 36.6739263393281],
                    [-119.57382202148439, 36.80598611937673],
                    [-119.73724365234375, 36.914764288955936],
                    [-119.92675781249999, 36.82357691815722]
                ]
            ]
      }, index='location')


Get nearest
===========

Get the documents closest to a specified GeoJSON ``Point`` based on proximity
to a geospatial index.

.. container:: example python

    .. code-block:: python

        Query('movies').get_nearest({
            'type': 'Point',
            'coordinates': [-118.35399627685547, 34.13759651725404]
        }, index='location')

.. container:: example javascript

    .. code-block:: javascript

        new Query('movies').getNearest({
            'type': 'Point',
            'coordinates': [-118.35399627685547, 34.13759651725404]
        }, 'location')
