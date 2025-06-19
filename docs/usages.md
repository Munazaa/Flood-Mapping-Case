## Usage

This project provides a streamlined approach to detect floods using Sentinel-1 and Sentinel-2 data. Below are the steps to use the project:

### Step 1: Set Up the Environment
- Clone the repository:  
  ```sh
  git clone https://github.com/your-username/Flood-Mapping-Case.git
  ```
   ```sh
  cd Flood-Mapping-Case
  
## Requirements

Install the required Python libraries using the following command:

```sh
pip install -r requirements.txt
```
<h2>Step 2: Configure the Project</h2>
<p>Edit the <code>config.ini</code> file and provide:</p>
<ul>
  <li><code>flood_date</code>: date of the flood event</li>
  <li><code>aoi_wkt</code>: AOI polygon in WKT format (rectangle preferred)</li>
  <li>Paths to input datasets (slope map, lakes, rivers)</li>
  <li>Output directory path</li>
  <li>Optional: DEM/slope thresholds, polarization type, etc.</li>
</ul>

<h2>Step 3: Run the Script</h2>
<p>Run the pipeline using:</p>
<pre><code class="language-bash">python main.py</code></pre>

<p>This script will:</p>
<ul>
  <li>Download Sentinel-1 and Sentinel-2 imagery</li>
  <li>Detect floods using NDWI (S2) and backscatter change (S1)</li>
  <li>Apply slope, elevation, and river/lake masking</li>
  <li>Save cleaned outputs as raster and shapefiles</li>
</ul>

<h2>Step 4: Access the Results</h2>
<ul>
  <li>
    Results are saved to the <code>output_directory</code> specified in <code>config.ini</code>
  </li>
  <li>
    Outputs include:
    <ul>
      <li>Flood masks (<code>.tif</code>)</li>
      <li>Vector shapefiles (<code>.shp</code>) of flooded areas</li>
    </ul>
  </li>
  <li>
    You can open them in <strong>QGIS</strong>, <strong>ArcGIS</strong>, or <strong>Google Earth Engine</strong> for further analysis
  </li>
</ul>

