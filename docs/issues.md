# Issues

The following open issues need to be fixed. Create a feature branch for each issue,
implement it, fix it and commit it. Decide with your colleague who is in charge in
merging the features into the `main` branch:

1. [ ] **Extract `CH4C` from summary database** (easy): Currently the `warming.data.summary.Summary` contains one
    method to retrieve data for `CO2C` (CO2 per capita per year). Create an additional functionality to
    to access the data for methane per capita per year (column `CH4C`).

2. [ ] **Extract `N2OC` from summary database** (easy): Currently the `warming.data.summary.Summary` contains one
    method to retrieve data for `CO2C` (CO2 per capita per year). Create an additional functionality to
    to access the data for methane per capita per year (column `N2OC`).

3. [ ] **Extract `CO2Y`, `CH4Y` and `N20Y` from summary database** (easy): Similar to issues **1** and **2** create
    methods which extract the values for a year.

4. [x] **Implement Europe map** (medium): Based on the `warming.plot.maps.World` create the new derived class
    `Europe`, which has the same methods, except that it only shows the European countries.

5. [ ] **Fix dataset** (medium): As you can see, when running the main file, some countries are not shown at all
    (e.g., "United Kingdom" vs. "United Kingdom of Great Britain and Northern Ireland").
    This is because of a mismatch between the country names in `warming.plot.maps.World` and
    `warming.data.summary.Summary`. Debug the data sets, figure out the differences and fix the problem.

6. [ ] **Recreate Extended Data Fig.3** (medium): As in the original paper
    [figure](https://www.nature.com/articles/s41558-023-01605-8/figures/7).

7. [ ] **Global projections**: Read the "Global Projections" sheet from the excel file and plot the
     `CO2`, `CH4` and `N2O` projections for each of the population projections.
     1. [ ] **Read the data**: Create a new module with a new class in the `warming.data` package
          which reads and prepares the data of the sheet.
     2. [ ] **Plot the data**: Create a new module in the `warming.plot` package with a class that
          gets data with a method and plots the data to get a figure which looks like
          [this](TBA).

## References

* [Ivanovich, C.C., Sun, T., Gordon, D.R. *et al.* Future warming from global food consumption.
*Nat. Clim. Chang.* **13**, 297–302 (2023).
https://doi.org/10.1038/s41558-023-01605-8](https://www.nature.com/articles/s41558-023-01605-8)
* [pandas documentation](https://pandas.pydata.org/docs/)
* [GeoPandas Doc](https://geopandas.org/en/stable/docs/user_guide/mapping.html)
  Documents the GeoPandas package which is used to show a (world) map.