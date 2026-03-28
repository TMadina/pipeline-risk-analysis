pipeline_layer=QgsProject.instance().mapLayersByName('pipeline')[0]
water_layer= QgsProject.instance().mapLayersByName('water')[0]

from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsField,QgsSpatialIndex

if 'lenght_m' not in [f.name() for f in pipeline_layer.fields()]:
    pipeline_layer.dataProvider().addAttributes ([QgsField('lenght_m', QVariant.Double)])

if 'risk_level' not in [f.name() for f in pipeline_layer.fields()]:
    pipeline_layer.dataProvider().addAttributes([QgsField ('risk_level', QVariant.String)])
    
    pipeline_layer.updateFields()

index = QgsSpatialIndex(water_layer.getFeatures())

with edit(pipeline_layer):

    for line in pipeline_layer.getFeatures():
        geom = line.geometry()
        line['lenght_m']= geom.length()
        bbox = geom.buffer (500,5).boundingBox()
        candidate_ids = index.intersects(bbox)
        
        min_distance = float('inf')
        
        for fid in candidate_ids:
            water = water_layer.getFeature(fid)
            dist = water.geometry().distance(geom)
            
            if dist < min_distance:
                min_distance = dist
                
        if line['substance'] in ['oil','gas','sulphur']:
            if min_distance <= 100:
                line ['risk_level'] ='high'
            elif min_distance <= 500:
                line['risk_level'] = 'medium'
            else:
                line['risk_level']= 'low'
        pipeline_layer.updateFeature(line)

high_len = 0
medium_len =0
low_len =0
for f in pipeline_layer.getFeatures():
    length = f['lenght_m']

    if f['risk_level'] == 'high':
        high_len += length
    elif f['risk_level'] == 'medium':
        medium_len += length
    else:
        low_len += length

total = high_len + medium_len + low_len
    

       
  

pipeline_layer.setRenderer(None)
pipeline_layer.triggerRepaint()


from qgis.core import QgsSymbol, QgsRendererCategory, QgsCategorizedSymbolRenderer
from PyQt5.QtGui import QColor

categories = []

symbol_high = QgsSymbol.defaultSymbol(pipeline_layer.geometryType())
symbol_high.setColor(QColor('red'))
categories.append(QgsRendererCategory('high', symbol_high, 'High Risk'))

symbol_medium = QgsSymbol.defaultSymbol(pipeline_layer.geometryType())
symbol_medium.setColor(QColor('yellow'))
categories.append(QgsRendererCategory('medium', symbol_medium, 'Medium Risk'))

symbol_low = QgsSymbol.defaultSymbol(pipeline_layer.geometryType())
symbol_low.setColor(QColor('green'))
categories.append(QgsRendererCategory('low', symbol_low, 'Low Risk'))

renderer = QgsCategorizedSymbolRenderer('risk_level', categories)


pipeline_layer.setRenderer(renderer)
pipeline_layer.triggerRepaint()

print('===PIPELINE RISK REPORT===')
print (f'Total length: {round(total,2)}m')
print (f'High risk: {round(high_len,2)}m ({round(high_len/total * 100,1)}%)')
print (f'Medium risk: {round(medium_len,2)}m ({round(medium_len/total * 100,1)}%)')
print (f'Low risk: {round(low_len,2)}m ({round(low_len/total * 100,1)}%)')











