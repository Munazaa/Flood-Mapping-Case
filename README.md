# Flood detection

- **Visualization and Analysis of Floods Using Satellite Data**: This project focuses on leveraging satellite imagery to detect flooded areas.

- **NDWI Calculation**: The code calculates the Normalized Difference Water Index (NDWI) using Sentinel-2 imagery to detect water bodies before and after a flood event.

- **SAR-Data Processing**: Sentinel-1 SAR data is processd in SNAP using snappy API.

- **Post-Processing Steps**: This version of the code provides an initial estimation of flood detection but requires further post-processing steps to enhance accuracy. These include refining the thresholds, integrating auxiliary datasets, and improving water body masking, which are currently underway.

- **Outputs**:
  - Flood-extent layers.
- **Vector (shapefile) and raster (.tif) outputs are saved to the specified path for further visualization and analysis in geospatial tools such as ArcGIS or QGIS.**

## Requirements
To install the required libraries, run the following command:

```sh
pip install -r requirements.txt
```
# Configuration File (config.ini)
The config.ini file is used to define parameters for the flood analysis.

```ini
[GENERAL]
before_event_start = YYYY-MM-DD       # Start date of the "before event" period
before_event_end = YYYY-MM-DD         # End date of the "before event" period
after_event_start = YYYY-MM-DD        # Start date of the "after event" period
after_event_end = YYYY-MM-DD          # End date of the "after event" period


[INPUT]
aoi = coordinates of the rectangle of the area or /path/to/aoi_shapefile.shp   # Path to Area of Interest (AOI) shapefile
s1_collection = COPERNICUS/S1_GRD       # Sentinel-1 ImageCollection ID or directly from GEE
s2_collection = COPERNICUS/S2_SR        # Sentinel-2 ImageCollection ID or directly from GEE
swater_dataset = JRC/GSW1_0/GlobalSurfaceWater  # Permanent water dataset or water data from other sources
chirps_start_date =  YYYY-MM-DD         #start month for rainfall analysis 
chirps_end_date =  YYYY-MM-DD          #end month for rainfall analysis 

[OUTPUT]
output_directory = /path/to/output        # Directory to save vector output
google_drive_folder = Flood_Analysis      # Google Drive folder to save exported files

