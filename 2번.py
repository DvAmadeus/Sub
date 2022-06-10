import numpy as np
import pandas as pd
from statsmodels.formula.api import ols,glm
import matplotlib.pyplot as plt


bodydata = pd.read_csv("bodyfat.csv",encoding='cp949')
MenBodyFat = bodydata[bodydata['Gender'] == 'M'][['BodyFat','Density']].set_index("Density");
WomenBodyFat = bodydata[bodydata['Gender'] == 'W'][['BodyFat','Density']].set_index("Density");
print(MenBodyFat)
print(WomenBodyFat)

plt.plot(MenBodyFat, label='bins=10')
plt.plot(WomenBodyFat, label='bins=30')
plt.legend()

plt.show()