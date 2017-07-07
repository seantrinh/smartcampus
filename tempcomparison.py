import MySQLdb
import sys
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

connection = MySQLdb.connect(host='danube.stevens.edu', user='pi2', passwd='yJPvf4iy', db='smartcampus')
cursor = connection.cursor()

cursor.execute("SELECT time, temp, temp2 FROM temppi1 WHERE date = '2017-07-01'")
data = cursor.fetchall()

time=[]
temp=[]
temp2=[]
diff=[]

for row in data:
    time += [str(row[0])]
    temp += [row[1]]
    temp2 += [row[2]]
    diff += [row[2]-row[1]]

cursor.close()
connection.close()

trace1 = go.Scatter(
    x = time,
    y = temp,
    name='Temp from BMP')

trace2 = go.Scatter(
    x = time,
    y = temp2,
    name='Temp from DHT22')

trace3 = go.Scatter(
    x = time,
    y = diff,
    name='Difference in Temperature Readings')
    
graphdata = [trace3]
layout = dict(title = 'Difference in Temperature Readings',
              xaxis = dict(title='Time'),
              yaxis = dict(title='Difference in Celsius', domain=[0, 2], scaleratio=0.1))
fig2 = dict(data=graphdata, layout=layout)
py.iplot(fig2, filename='tempdifference')
sys.exit()
