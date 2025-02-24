# batch7_satellite_ges

* /dataset contains a sample of OCO-2 data and inventory data;
* /notebooks contains the notebooks make by the team;
* /pipeline contains the scripts used to generate the data needed.

# General presentation

The goal of our project is to localize CO² emissions on Earth based on the the carbon concentration data measured by the OCO-2 Satellite from the NASA. 

We are working with:
- Matthieu Porte, from IGN who submit the projet
- Marie Heckmann, from the French Ministry of Ecology
- Frederic Chevalier, from IPSL, one of the author of <https://www.atmos-chem-phys-discuss.net/acp-2020-123/acp-2020-123.pdf>

# What we have as input

**1/ OCO-2 Satellite data**

The OCO-2 Satellite (Orbiting Carbon Observatory) from the NASA orbits around Earth and measures the CO² concentration in the atmosphere.  

Here is a visualisation of the CO² concentration mesured by the OCO-2 satellite in December 2019. 
![CO2_ concentration_OCO2](https://user-images.githubusercontent.com/61688979/79854803-4c012f80-83ca-11ea-921e-49dcbf55440f.PNG)

The satellite uses spectrometers to detect CO² in the atmosphere, as shown in the image bellow. 
![OCO2 spectrometers](https://oco.jpl.nasa.gov/media/uploads/2019/05/07/oco_column.jpg)

More info here : <https://oco.jpl.nasa.gov/instrument/>

There are some limitations to the satellite measurement of the CO² concentration:
- The satellite can not see through clouds or fog;
- It does not work the same over ground or water;
- The swath of the satellite is quite narrow (only 10km), as shown in the image bellow; 
- As the satellite orbits the Earth, the coverage is partial.

![OCO2 spectrometers](https://scx1.b-cdn.net/csz/news/800/2020/3-nasasatellit.jpg)
!!

More info on the mission on <https://earth.esa.int/web/eoportal/satellite-missions/o/oco-2>.

The NASA made a global CO² image (see bellow), however this is an extrapolation of the data, and not what the satellite really see.

![NASA Global CO²](https://www.jpl.nasa.gov/images/oco/20090219/sinks-browse.jpg)

**2/ Data on known CO2 emissions**

- The Emissions Database for Global Atmospheric Research (EDGAR) on CO² emissions. For the energy related sectors the activity data is mainly based on the energy balance statistics of IEA (2017), whereas the activity data for the agricultural sectors originates mainly from FAO (2018). The spatial allocation of emissions on the grid is made based on spatial proxy datasets with the location of energy and manufacturing facilities, road networks, shipping routes, human and animal population density and agricultural land use, that vary over time. 
Source : https://edgar.jrc.ec.europa.eu/overview.php?v=50_GHG

![CO2_emissions_Edgar_2018](https://user-images.githubusercontent.com/61688979/79775474-9637d180-8334-11ea-9712-274a11356aea.PNG)

- The World Resource Institute provides a list of power plants producing electricity based on different primary energies. We filtered this list to keep only the fossil primary energies (gas, oil and coal), that release CO² during their combustion.
Source: http://datasets.wri.org/dataset/globalpowerplantdatabase

![power_plant_emissions_2017](https://user-images.githubusercontent.com/61688979/79775550-b5366380-8334-11ea-9587-8d42b241160e.PNG)

- Other sources of CO² emissions are under study. 

# What we want to do


First approach: peak detection from O-CO2 & inference from inventory data [in progress]

- Detect peak in O-CO2 data, 2 step methodology
	- Step 1: Identification of local ‘peaks’ through Gaussian fits (curve_fit) ; Taking into account intrinsic complexity of O-CO2 data, notably: High variance across ‘background’ CO² level across the globe, narrowness & incompleteness of plumes observations (due to clouds / fogs / …), ...
	- Step 2: Elimination of irrelevant peaks to keep only ‘true’ anomalies: So far, through a quite drastic & manual methodology, with rules to keep only clear Gaussians ; Objective to improve this part with algo-based anomaly detection 

- Aggregate known sources of CO² from inventory data: Using EDGAR & World Resource Institute

- Find nearest inventory from peak position, using the wind vector.

- Compare peak to known sources emissions and confirm them

Second approach: supervised model to learn to detect peaks from inventory data [not started]
- Use areas where inventory data are complete to let a supervised model learn peaks in OCO2 data

On top: dynamic visualization of data [in progress]
- Display the result on a comprehensive map, crossing satellite & inventory data

# What we have achieved

 - We gather data from EDGAR and World Resource Institute and plotted them on a map.
 - We get raw satellite data from NASA and merge the to monthly dataset with the data we need.
 - We compute a Gaussian curve fit over each orbit and save the results.
 - We plot the results and the know emission on a map.

Here is a sample of a peak witth the gaussian found :
![CO2_peak of Laiwu](https://github.com/dataforgoodfr/batch7_satellite_ges/raw/master/image.png)

And the global map :
![World CO2_peaks](https://github.com/dataforgoodfr/batch7_satellite_ges/raw/master/map-dark.png)
![CO2_peak over Spain](https://github.com/dataforgoodfr/batch7_satellite_ges/raw/master/map-dark-orbit.png)


# We need help

- Better peak detection: So far, we are fitting Gaussian curves to detect relevant peaks. 2 issues:
    - We use SciKit Learn curve_fit. Do you know a better algorithme or how to tune parameters of curve_fit ?
    - We are looking at other methodologies to detect anomalies (our 'peaks') in the concentrations  - any idea? 
- Wind modeling to estimate emission from detected concentration - any idea? (inverting the Gaussian plume model)
- Interactive dasboard to share our work on the web (Streamlit ?)
