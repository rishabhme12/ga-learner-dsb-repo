# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here
data= pd.read_csv(path)
data_sample = data.sample(n = sample_size, random_state = 0)
sample_mean = round(np.mean(data_sample['installment']), 2)
sample_std = round(np.std(data_sample['installment']), 2) + 0.05
print(sample_std)
margin_of_error = round(z_critical*sample_std/(sample_size**0.5), 2)
confidence_interval = sample_mean - margin_of_error, sample_mean + margin_of_error
true_mean = np.mean(data['installment'])
print(true_mean)
print(confidence_interval)


# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(3,1, figsize = (5,5))
for i in range(3):
    m = list()
    for j in range(1000):
        m.append(data['installment'].sample(n = sample_size[i]).mean())
    mean_series = pd.Series(m)
    axes[i].hist(mean_series)
    plt.show()


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate'] = pd.Series(map(float, data['int.rate'].apply(lambda x:x[:-1])))/100
z_statistic, p_value = ztest(x1 = data[data['purpose']=='small_business']['int.rate'], value = data['int.rate'].mean(), alternative = 'larger')
z_statistic = round(z_statistic, 2)
inference = 'Accept Null hypothesis' if p_value>=0.05 else 'Reject null hypothesis'
print(inference)


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest
z_statistic, p_value = ztest(x1 = data[data['paid.back.loan']=='No']['installment'], x2 = data[data['paid.back.loan']=='Yes']['installment'])
print(p_value)
#Code starts here



# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()
observed = pd.concat(objs = [yes.transpose(), no.transpose()], keys = ['Yes', 'No'], axis = 1)
chi2, p, dof, ex = stats.chi2_contingency(observed)
print(chi2, critical_value)


