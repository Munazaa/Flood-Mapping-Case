#Importing Libraries

import os
import sys
os.environ['SNAP_HOME'] = r"C:\Program Files\esa-snap" #snappy.py path
from snappy import ProductIO, GPF, HashMap, jpy
from config import OUTPUT_FOLDER, POLARIZATION
from config import S1_ZIP_PATH, SHAPEFILE_PATH, OUTPUT_PATH
from snappy import ProductIO, GPF, HashMap, WKTReader, jpy
import shapefile
from shapely.geometry import shape, MultiPolygon
import pygeoif
from glob import glob

# User defined parameters
## For single ZIP test

S1_ZIP_PATH = "data/S1B_IW_GRDH_1SDV_20201004T171410_20201004T171435_023666_02CF75_467F.SAFE.zip"

# For batch processing uncomment below
#ZIP_FOLDER = "data/sentinel_zips"
#ZIP_FILES = glob(os.path.join(ZIP_FOLDER, "*.zip"))
# Output filename (without .tif)
OUTPUT_PATH = "data/final_mask"
FLOOD_DATE = "2020-10-02"
POLARIZATION = "VV"

SHAPEFILE_PATH = "data/Alto-Garda.shp" #define AOI coordinates or shapefile
OUTPUT_FOLDER = "data/flood_outputs"

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)



#Procssing on the folders 

def shp_to_wkt(shp_path):
    r = shapefile.Reader(shp_path)
    shapes = [shape(s.__geo_interface__) for s in r.shapes()]
    merged = MultiPolygon(shapes)
    return merged.wkt

def load_product(path):
    return ProductIO.readProduct(path)

def apply_orbit(product):
    params = HashMap()
    params.put('orbitType', 'Sentinel Precise (Auto Download)')
    params.put('polyDegree', '3')
    params.put('continueOnFail', 'false')
    return GPF.createProduct('Apply-Orbit-File', params, product)

def subset(product, shapefile_path):
    wkt = WKTReader().read(shp_to_wkt(shapefile_path))
    params = HashMap()
    params.put('copyMetadata', True)
    params.put('geoRegion', wkt)
    return GPF.createProduct('Subset', params, product)

def calibrate(product):
    params = HashMap()
    params.put('outputSigmaBand', True)
    params.put('sourceBands', 'Intensity_VV')
    params.put('selectedPolarisations', 'VV')
    params.put('outputImageScaleInDb', False)
    return GPF.createProduct('Calibration', params, product)

def speckle_filter(product):
    params = HashMap()
    params.put('sourceBands', 'Sigma0_VV')
    params.put('filter', 'Lee')
    params.put('filterSizeX', '5')
    params.put('filterSizeY', '5')
    return GPF.createProduct('Speckle-Filter', params, product)

def terrain_correction(product):
    params = HashMap()
    params.put('demName', 'SRTM 3Sec')
    params.put('pixelSpacingInMeter', 10.0)
    return GPF.createProduct('Terrain-Correction', params, product)

def flood_mask(product):
    BandDescriptor = jpy.get_type('org.esa.snap.core.gpf.common.BandMathsOp$BandDescriptor')
    bd = BandDescriptor()
    bd.name = 'flooded'
    bd.type = 'uint8'
    bd.expression = '(Sigma0_VV < 1.13E-2) ? 1 : 0'
    bands = jpy.array('org.esa.snap.core.gpf.common.BandMathsOp$BandDescriptor', 1)
    bands[0] = bd
    params = HashMap()
    params.put('targetBands', bands)
    return GPF.createProduct('BandMaths', params, product)

def run_pipeline(image_zip, shapefile_path, output_path):
    GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
    p = load_product(image_zip)
    p = apply_orbit(p)
    #p = subset(p, shapefile_path)
    p = calibrate(p)
    p = speckle_filter(p)
    p = terrain_correction(p)
    p = flood_mask(p)
    ProductIO.writeProduct(p, output_path, 'GeoTIFF')
    print(" Flood layer saved to:", output_path + ".tif")

# ---- Run the pipeline using config values ----
run_pipeline(S1_ZIP_PATH, SHAPEFILE_PATH, OUTPUT_PATH)
