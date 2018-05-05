import pandas.tseries
import pandas as pd
import statsmodels.api as sm
import numpy as np
np.warnings.filterwarnings("ignore")
np.warnings.resetwarnings()
# from scipy import stats

df1 = pd.read_csv('C:/Users/humei/Desktop/Python T,T/analysis/Twitch_Sentiment.csv')
df2 = pd.read_csv('C:/Users/humei/Desktop/Python T,T/analysis/YouTube_Sentiment.csv')
#df1.head()


# linear regression

#get data that its sentiment bigger than 0.5 for twitch
hs = df1['x']>0.5
hdf = df1[hs]
X=  hdf['x']
y = hdf['y']
#X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print(model.summary())
#plt.show()

#get correlation
print(hdf['y'].corr(hdf['x']))
print(hdf.corr())

#get data that its sentiment bigger than 0.5 for youtube
hs2 = df2['x']>0.5
hdf2 = df2[hs2]
X2=  hdf2['x']
y2 = hdf2['y']
model = sm.OLS(y2, X2).fit()
predictions = model.predict(X2) # make the predictions by the model

# Print out the statistics
print(model.summary())
#plt.show()

#get correlation
print(hdf2['y'].corr(hdf2['x']))
print(hdf2.corr())



#get data that its sentiment less than 0.5 for twitch
ls = df1['x']<0.5
ldf = df1[ls]
X=  ldf['x']
y = ldf['y']

model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print(model.summary())
#plt.show()

#get correlation
print(ldf['y'].corr(ldf['x']))
print(ldf.corr())

#get data that its sentiment lower than 0.5 for yotube
ls2 = df2['x']<0.5
ldf2 = df2[ls2]
X2=  ldf2['x']
y2 = ldf2['y']
model = sm.OLS(y2, X2).fit()
predictions = model.predict(X2) # make the predictions by the model

# Print out the statistics
print(model.summary())
#plt.show()

#get correlation
print(ldf2['y'].corr(ldf2['x']))
print(ldf2.corr())























