from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


#Latittud y longitud de los puntos Mexico, Argentina y la quinta avenida de NY 
lat=[19.4326009, -34.9964962, 40.7410861]
lon=[-99.1333415, -64.9672816, -73.9896297241625]


#Dimension de la figura
plt.figure(figsize=(16,12))


#Se inicializa el tipo de cartografia, la resolucion y 
eq_map=Basemap(projection="robin",
               lon_0=0,
               resolution="h",
               area_thresh=1000.0,
               llcrnrlon=-136.25,
               llcrnrlat=56,
               urcrnrlon=-134.25,
               urcrnrlat=57.75)


#Dibuja lieas costeras y paises
eq_map.drawcoastlines()
eq_map.drawcountries()


#Color de los paises 
eq_map.fillcontinents(color="e6e6ff")
eq_map.drawmapboundary()


#Se dinujan meridianos y paralelos
eq_map.drawmeridians(np.arange(0,360,30))
eq_map.drawparallels(np.arange(-90,90,30))


#Se dibujan los puntos con zip que empaqueta varias listas y las itera paralelamente
for lon, lan in zip(lon,lat):
    x,y=eq_map(lon,lat)
    
    
#Se traza un circulo color rojo (ro)con un radio de 17 y una transparencia de 0.8
    eq_map.plot(x,y,"ro",makersize=17,alpha=0.8)
    
    
#Se guarda la imagen en formato png
plt.savefig("visualizacionDatos.png", bbox_inches="tight",dpi=100)

