from mpl_toolkits.basemap import Basemap
import matplotlib.pylplot as pl
import scipy as sp
import threading

class mapPlotEvent(threading.Thread):
	"""Class for plotting of events on a map"""
	def __init__(self, projMap):
		"""Initiate background map, projection given"""
		h = 10000 #### Random Scalar for height of view
		minSize = 5.0
		mapBackgroud = Basemap(projection=projMap, lon_0=centrelon, lat_0=centreLat, satellite height=h*1000)
		### Draw map outline and fill colour
		mapBackground.drawcoastlines()
		mapBackground.drawmapboundary(fll_color="aqua")
		mapBackground.fillcontinents(color="blue", lake_color="aqua")

	def plotEvent(eventInput):
		"""Plots an event on our projection of choice"""
		xplt, yplt = mapBackground(eventInput.lon, eventInput.lat)
		m.scatter(xplt, yplt, marker="o", markersize = minSize*eventInput.data)

	def showMap():
		pl.show()

	def clearMap():
		pl.clf()
		
