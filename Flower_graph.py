#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ploting flower species
#import libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show, save
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool


# difine the output file path
output_file("iris.html")




#create the figure object

f=figure()

#Style the tool
f.tools =[PanTool(), ResetTool()]
f.add_tools(hover)
f.toolbar_location = 'above'
f.toolbar.logo=None
hover=HoverTool(tooltips=[('Species','@species'),('Sepal width', '@sepal_width')])

# stylize the plot aria
f.plot_width = 1100
f.plot_height = 650
f.background_fill_color ='pink'
f.background_fill_alpha =0.3
f.border_fill_color = 'pink'
f.border_fill_alpha=0.5

#style the title

f.title.text = "Iris Flowers"
f.title.text_color = 'green'
f.title.text_font= 'times'
f.title.text_font_size = "18px"
f.title.align = 'center'
f.xaxis.minor_tick_line_color = 'blue'
f.yaxis.major_label_orientation = 'horizontal'
f.xaxis.visible = True
f.xaxis.minor_tick_line_color = 'red'
f.xaxis.minor_tick_in = -10
f.xaxis.axis_label ='Petal Length'
f.yaxis.axis_label = 'Petal Width'
f.axis.axis_label_text_color= 'blue'
f.axis.major_label_text_color = 'purple'

#Axis geometry

f.x_range = Range1d(start = 0, end = 10)
f.y_range= Range1d(start = 0, end = 5)
f.xaxis.bounds = (2,5)
f.xaxis[0].ticker.desired_num_ticks = 2
f.yaxis[0].ticker.desired_num_ticks = 2
f.yaxis[0].ticker.num_minor_ticks = 10

#Style grid
f.xgrid.grid_line_color = None
f.ygrid.grid_line_alpha= 0.3
f.grid.grid_line_dash=[5,3]

# Create an extra colomn in data, by creating map(dict)
colormap = {'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
flowers['color']=[colormap[x] for x in flowers['species']]



#adding glyphs
f.circle(x=flowers['petal_length'][flowers['species']=='setosa'], y=flowers['petal_width'][flowers['species']=='setosa'],
            size=flowers['sepal_width'][flowers['species']=='setosa']*3,
             fill_alpha=0.2, color=flowers['color'][flowers['species']=='setosa'],line_dash=[5,3], legend = 'Setosa')
                                                
                                                
f.circle(x=flowers['petal_length'][flowers['species']=='versicolor'], y=flowers['petal_width'][flowers['species']=='versicolor'],
        size=flowers['sepal_width'][flowers['species']=='versicolor']*3,
         fill_alpha=0.2, color=flowers['color'][flowers['species']=='versicolor'],line_dash=[5,3], legend = 'Versicolor')
                                                
f.circle(x=flowers['petal_length'][flowers['species']=='virginica'], y=flowers['petal_width'][flowers['species']=='virginica'],
        size=flowers['sepal_width'][flowers['species']=='virginica']*3,
         fill_alpha=0.2, color=flowers['color'][flowers['species']=='virginica'],line_dash=[5,3], legend = 'Virginica')



show(f)
         


    


# In[3]:


dir(f.legend)


# In[73]:


flowers


# In[67]:


flowers['sepal_width']*5


# In[74]:


colormap = {'setosa':'red', 'versicolor':'green', 'virginica':'blue'}


# In[76]:


[colormap[x] for x in flowers['species']]


# In[81]:


flowers['petal_length'][flowers['species']=='setosa']


# In[105]:


dir(f.legend)


# In[ ]:




