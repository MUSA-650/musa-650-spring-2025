# Lab: Importing and Visualizing Satellite Datasets

## Objective

This lab introduces you to importing and visualizing geospatial datasets using `planetary_computer` and `xarray`. You will work in groups of 2-3 people to query satellite imagery, explore its bands, and visualize the data using `matplotlib`. This exercise also highlights how remote sensing can provide critical insights into land cover, urban development, and environmental change, supporting urban planning, disaster response, and resource management.

## Instructions

Use the tutorial from the following link as the basis for your work: [Project Pythia Landsat ML Cookbook - Data Ingestion](https://projectpythia.org/landsat-ml-cookbook/notebooks/1.0_Data_Ingestion-Geospatial.html). While the tutorial provides an interactive visualization option, we recommend using regular `matplotlib` for your visualizations in this lab.

## Steps

1. **Connect to `planetary_computer`**  
   Set up a connection to the Planetary Computer API.

2. **List the Available Collections**  
   Explore and print all datasets available from the API.

3. **Retrieve Landsat 8 Imagery**  
   Retrieve Landsat 8 imagery for Cairo, Egypt, between '2024-06-01' and '2024-08-31'. Use the interactive `Panel` viewer to explore the retrieved images:

   ```
   # Step 3: Preview Items (Optional)
   item_id = {(i, item.id): i for i, item in enumerate(items)}
   item_sel = pn.widgets.Select(value=0, options=item_id, name="Select Item")

   def get_preview(i):
       return pn.panel(items[i].assets["rendered_preview"].href, height=300)

   pn.Row(item_sel, pn.bind(get_preview, item_sel)).servable()
   ```

4. **Examine Metadata and Bands**  
   Select and examine the metadata of the first image (e.g., type, ID, geometry, bbox, properties, assets, etc.). List all the bands in the image, including their names and descriptions. Make sure to include the `qa_pixel` band for cloud masking.

5. **Cloud Cover Analysis**

   - Merge the tiles spatially to create a single image per time step: `ds_merged = xr.concat(datasets, dim="time")`.
   - Calculate the **average, minimum, maximum, and standard deviation** of per-pixel cloud cover across all images.
   - Create a single composite image of all the images by taking the median (`ds_composite = ds_merged.median(dim="time")`).
     - Hint: Set the `attrs` of your data array, including the CRS, to maintain spatial consistency.

6. **Summary Statistics**  
   Return the **mean, minimum, maximum, and standard deviation** of each band for the final composite image.

7. **Visualization**
   - Plot each of the red, green, and blue bands in greyscale using `matplotlib`.
   - Combine the bands to create and plot a composite RGB image in color.

## Deliverables

All code, visualizations, and analyses should be included in a single Jupyter Notebook.

## Important Note

We will reuse code and concepts from this assignment in future labs and homeworks. Completing this lab thoroughly and saving your work will significantly benefit you later in the course.
