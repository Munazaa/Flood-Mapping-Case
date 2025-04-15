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
### Step 2: Configure the Project
Edit the config.ini file located in the repository to set the analysis parameters:
- Dates for "before" and "after" events to download satellite data.
- Paths to the input datasets in Datalake (e.g., Artifacts, AOI shapefile, DEM, Rivers and lakes shapeffiles).
- Output directory for saving results.

 ### Step 3: Run the Jupyter Notebook
Open the notebook located in the [`src`](src/) folder. Click the link to view and download the notebook.
```sh
jupyter notebook src/flood_detection_notebook.ipynb
```
- Run the notebook cells sequentially.
- Visulize the pre and post water detection layers for each satellite data.
- Analyze Sentinel-1 and Sentinel-2 data for flood detection.
 ### Step 4: Access the Results

- Exported Files: The results (shapefile) will be saved in the directory specified in the config.ini file.
- Use geospatial tools such as QGIS or ArcGIS for further visualization and analysis of the outputs.
