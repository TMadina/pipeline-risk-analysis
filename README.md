# pipeline-risk-analysis
Pipeline risk assessment using QGIS and Python
# Pipeline Risk Assessment Near Water Bodies

## 📍 Overview

This project presents a spatial analysis of pipeline risk based on proximity to water bodies.
The goal is to identify potentially hazardous pipeline segments that could impact nearby water resources.

## 🧠 Objective

To classify pipelines into risk categories based on their distance to rivers and lakes using GIS and Python automation.

## 🗂️ Data

* Pipeline data: OpenStreetMap (OSM)
* Water bodies: OpenStreetMap (OSM)
* Study area: Alberta, Canada

## ⚙️ Methodology

The analysis was performed using QGIS and PyQGIS:

1. Extracted pipeline and water layers from OSM
2. Built a spatial index for efficient spatial queries
3. Calculated minimum distance from each pipeline segment to nearest water body
4. Classified risk levels:

   * **High Risk**: ≤ 100 meters
   * **Medium Risk**: 100–500 meters
   * **Low Risk**: > 500 meters
5. Calculated total pipeline length per risk category
6. Applied categorized symbology for visualization

## 📊 Results

* Total pipeline length: 2,545,570 m
* High Risk: 1,167,163 m (45.9%)
* Medium Risk: 75,991 m (3.0%)
* Low Risk: 1,302,416 m (51.2%)

## 🗺️ Map

![Pipeline Risk Map](map/pipeline_risk_map.png)

## 📁 Output Data

A cleaned dataset with selected attributes is available:

* `id`
* `substance`
* `length_m`
* `risk_level`

See: `data/pipeline_risk_sample.csv`

## 💻 Code

The full PyQGIS script is available in:
`code/data_generation.py`

## 🚀 Key Skills Demonstrated

* Spatial analysis (buffer, distance, intersection)
* GIS automation with Python (PyQGIS)
* Data processing and cleaning
* Risk modeling and classification
* Cartographic visualization

## 📌 Conclusion

The analysis shows that a significant portion of pipelines is located near water bodies, indicating potential environmental risks.
This workflow can be adapted for environmental monitoring and infrastructure risk assessment.

