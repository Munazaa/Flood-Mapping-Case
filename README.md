# Flood detection

- **Visualization and Analysis of Floods Using Satellite Data**: This project focuses on leveraging satellite imagery to detect flooded areas.

- **NDWI Calculation**: The code calculates the Normalized Difference Water Index (NDWI) using Sentinel-2 imagery to detect water bodies before and after a flood event.

- **SAR-Data Processing**: Sentinel-1 SAR data is processd in SNAP using SNAPISTA.

- **Post-Processing Steps**: This version of the code provides an initial estimation of flood detection but requires further post-processing steps to enhance accuracy. These include refining the thresholds, integrating auxiliary datasets, and improving water body masking, which are currently underway.

- **Outputs**:
  - Flood-extent layers.
- **Vector (shapefile) and raster (.tif) outputs are saved to the specified path for further visualization and analysis in geospatial tools such as ArcGIS or QGIS.**

## Requirements
To install the required libraries, run the following command:

```sh
pip install -r requirements.txt
```

## 📂 Folder Structure

```plaintext
data/
├── Lakes_TN/                -> Trentino lakes shapefile (e.g. idrspacq.shp)
├── Rivers_TN/               -> Trentino rivers shapefile (e.g. cif_pta2022_v.shp)
├── sentinel_zips/           -> Sentinel-1 ZIP archives (GRD format)
├── sentinel2/
│   ├── Sentinel-2(Pre-NDWI)/  -> NDWI TIFFs before flood
│   └── Sentinel-2(Post-NDWI)/ -> NDWI TIFFs after flood
├── slope_TN/                -> Slope map for masking (GeoTIFF)
├── flood_outputs/           -> All final outputs (S1, S2, masks, metadata)
```

# How to Run

```python
# INPUT DATA
aoi_geometry = "<WKT_POLYGON>"  # User-defined AOI (rectangle recommended)
s1_collection = "COPERNICUS/S1_GRD"  # Sentinel-1 collection
s2_collection = "COPERNICUS/S2_SR"   # Sentinel-2 collection
slope_path = "slope_TN/slope.tif"    # Slope map path
lakes_dataset = "Lakes_TN/lakes.shp"  # Lakes shapefile
rivers_dataset = "Rivers_TN/rivers.shp"  # Rivers shapefile

# USER DEFINED PARAMETERS
params = {
    "Geometry": aoi_wkt,              # AOI defined by user (always give rectangle)
    "target_crs": "EPSG:25832",       # Don't change it for Trentino
    "flood_date": datetime.datetime.strptime("20201002", "%Y%m%d"),
    "polarization": ["VV", "VH"],     # ["VV"] or ["VH"] or both; both is good for flood detection
    "dem_threshold": 600,             # 500–1000
    "slope_threshold": 9,             # 5–20
    "noise_min_pixels": 7,            # 5–20, change accordingly
    "river_buffer_meters": 1          # 1–4 meters
}

# RUN
python main.py

# OUTPUT
output_directory = "/path/to/flood_outputs"        # Directory to save output


