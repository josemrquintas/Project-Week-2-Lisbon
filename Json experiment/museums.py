
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import geopy
from geopy.geocoders import Nominatim


# In[17]:


museums = pd.read_csv('museus.csv')
museums.head()


# In[24]:



geolocator = Nominatim(user_agent="UPS")
location = geolocator.reverse("38.717738, -9.150320")

museums['MORADA'] = [geolocator.reverse(str(museums['Y'][i]) + ', ' + str(museums['X'][i])) for i in range(len(museums['X']))]
museums.head()



# In[31]:



lst_freguesias = [(str(museums['MORADA'][i]).split(',')[x] for i in range(len(museums['MORADA'])) for x in range(len(str(museums['MORADA'].split(','))-1)) if (str(museums['MORADA'][i]).split(',')[x+1] == ' Lisboa' ]
lst_freguesias

