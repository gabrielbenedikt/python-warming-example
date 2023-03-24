import matplotlib.pyplot as plt
import geopandas as gpd


class Europe:
    """This class contains all the methods to visualize data on a map of europe"""

    def __init__(self):
        self._europe = gpd.read_file(
            gpd.datasets.get_path('naturalearth_lowres')
        )
        self._europe = self._europe[self._europe.continent == 'Europe']

    def show(self, data, column):
        """Opens a plot of a map of europe.

        The map shows the specified data, which also needs to be
        set with the `column` parameter.

        :param data: The data that will be shown on the map.
        :type data: pandas.core.series.Series
        :param column: The index of the data to show.
        :type column: str
        """

        vis_data = self._europe.join(data, on="name")
        vis_data.plot(column=column, cmap='OrRd')

        plt.show()

    def get_data(self):
        """Getter to retreive the geopandas 'naturalearth_lowres' data set

        :return: World data, filled with information of a country's population, GDP, geometry
        :rtype: geopandas.geodataframe.GeoDataFrame
        """
        return self._europe


class World:
    """This class contains all the methods to visualize data on a world map"""

    def __init__(self):
        self._world = gpd.read_file(
            gpd.datasets.get_path('naturalearth_lowres')
        )

    def show(self, data, column):
        """Opens a world map plot.

        The map shows the specified data, which also needs to be
        set with the `column` parameter.

        :param data: The data that will be shown on the world map.
        :type data: pandas.core.series.Series
        :param column: The index of the data to show.
        :type column: str
        """

        vis_data = self._world.join(data, on="name")
        vis_data.plot(column=column, cmap='OrRd')

        plt.show()

    def get_data(self):
        """Getter to retreive the geopandas 'naturalearth_lowres' data set

        :return: World data, filled with information of a country's population, GDP, geometry
        :rtype: geopandas.geodataframe.GeoDataFrame
        """
        return self._world
