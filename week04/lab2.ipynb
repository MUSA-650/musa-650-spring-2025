# Lab: Supervised Land Cover Classification with Landsat 8 and NLCD Data

## Objective

In this lab, you will:

1. Set up and authenticate Google Earth Engine (GEE) using geemap
2. Load and preprocess Landsat 8 imagery for San Francisco
3. Retrieve and prepare National Land Cover Dataset (NLCD) training data
4. Implement supervised classification using Random Forest models
5. Evaluate model performance across different training sample sizes
6. Classify a Landsat 8 image and compare results with ground truth NLCD data

---

**Important:** this lab is based very closely on [Dr. Qiusheng Wu's NLCD tutorial](https://geemap.org/notebooks/32_supervised_classification/). You will benefit from adapting it for your work.

## Instructions

### 1. GEE and geemap Setup

- Install required libraries: `geemap`, `ee`, `numpy`, `matplotlib`
- Authenticate Google Earth Engine
- Initialize Earth Engine with your Google Cloud Project
- Verify successful authentication and initialization

```
import ee
import geemap

ee.Authenticate()
ee.Initialize(project='your-google-project')
```

### 2. Landsat 8 Image Selection and Preprocessing

- Define a point geometry for San Francisco:
  - Coordinates: [-122.4439, 37.7538]
- Select a Landsat 8 image with the following criteria:
  - Collection: LANDSAT/LC08/C02/T1_L2
  - Date range: January 1, 2016 to December 31, 2016
  - Sort by lowest cloud cover

The path to the dataset has changed since Dr. Wu wrote his tutorial, so it now looks like this:

```
point = ee.Geometry.Point([-122.4439, 37.7538])

image = (
    ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
    .filterBounds(point)
    .filterDate("2016-01-01", "2016-12-31")
    .sort("CLOUD_COVER")
    .first()
    .select("SR_B[1-7]")
)
```

- Select spectral bands 1-7 (SR_B1 through SR_B7)

**Analytic Question**:  
Why is it important to select an image with low cloud cover? How might cloud cover impact land cover classification?

### 3. NLCD Data Preparation

- Load National Land Cover Dataset (NLCD)
- Clip NLCD data to the geometry of the selected Landsat 8 image
- Visualize the NLCD land cover classification for the area

**Analytic Question**:  
What land cover classes are present in the San Francisco area? How diverse is the landscape?

### 4. Random Forest Model Training

- Implement iterative Random Forest model training with different sample sizes:
  1. 10 training points
  2. 100 training points
  3. 1,000 training points
  4. 10,000 training points
- For each model iteration:
  - Calculate and plot accuracy scores
  - Calculate and plot Kappa coefficient
  - Document observations about model performance

**Analytic Questions**:

- How does the number of training samples impact model accuracy?
- At what point does increasing sample size cease to improve model performance significantly?
- What are the limitations of using Random Forest for land cover classification?

### 5. Land Cover Classification

- Use the Random Forest model trained on 10,000 points to classify the entire Landsat 8 image
- Apply the correct color palette for land cover classes
- Add the NLCD legend to the map for reference

### 6. Model Validation and Comparison

- Compare the classified image with the ground truth NLCD data
- Identify and discuss:
  - Areas of agreement
  - Potential misclassifications
  - Possible reasons for discrepancies

**Analytic Questions**:

- What factors might contribute to misclassifications?
- How reliable is this supervised classification method?
- What additional preprocessing or techniques could improve classification accuracy?

---

## Deliverables

1. A Jupyter Notebook with all code, visualizations, and analyses.
2. Responses to analytic questions embedded in the notebook.

## Collaboration Policy

Work in groups of 2-3 people.
