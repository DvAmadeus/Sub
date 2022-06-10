
import pandas as pd
from statsmodels.formula.api import ols


bodydata = pd.read_csv("bodyfat.csv",encoding='cp949')
columnslist = bodydata.columns
columnslist = columnslist.difference(["BodyFat"])
str = "BodyFat ~ "
for i in columnslist:
    str += i+"+"
str = str[:-1]
result = ols(str,data=bodydata).fit()
SampleDF = bodydata[bodydata.columns.difference(['BodyFat'])][0:3]
predict = result.predict(SampleDF)

print("--------------샘플 데이터-------------\n{0}\n----------------------------------".format(SampleDF))
print("--------------예측 결과-------------\n{0}\n----------------------------------".format(predict))