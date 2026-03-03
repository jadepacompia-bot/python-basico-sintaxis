#Jade Pacompia
#fechas en python
from datetime import date, datetime
#fecha actual
hoy = date.today()
print(hoy)
#Formatear fecha
formateado = hoy.strftime("%d/%m/%y")
print(formateado)
#hora actual
fecha_actual = datetime.now()
print(fecha_actual)
#capturar el año
year = fecha_actual.year
print(year)
mes = fecha_actual.month
print(mes)
dia = fecha_actual.day
print(dia)
hora_actual = fecha_actual.strftime("%H:%M:%S")
print(hora_actual)
#Formato AM - PM
hora_am_pm = fecha_actual.strftime("%I:%M:%S %p")
print(hora_am_pm)