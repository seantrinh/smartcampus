import MySQLdb
import sys
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

connection = MySQLdb.connect(host='192.168.1.240', user='pi2', passwd='smartcampus', db='wifi')
cursor = connection.cursor()

cursor.execute('SELECT time, download, upload FROM wifi')
data = cursor.fetchall()

time=[]
download=[]
upload=[]
for row in data:
    time += [str(row[0])]
    download += [row[1]]
    upload += [row[2]]

cursor.close()
connection.close()

trace1 = go.Scatter(
    x = time,
    y = download)
    #mode = 'markers')

trace2 = go.Scatter(
    x = time,
    y = upload)
    #mode = 'markers')

fig = tools.make_subplots(rows=1, cols=1, #specs=[[{}],[{}]],
                          shared_xaxes=True,shared_yaxes=True,
                          vertical_spacing = 0.001)
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 1)

fig['layout'].update(height = 800, width = 800, title='downloadupload')
py.iplot(fig, filename='downloadupload')
sys.exit()
