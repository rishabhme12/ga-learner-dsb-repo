# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = (df[df.fico>700].fico).size/df.fico.size
print(f'p_a:{p_a}')
p_b = df[df.purpose == 'debt_consolidation'].purpose.size/df.purpose.size
print(f'p_b:{p_b}')
df1 = df[df.purpose =='debt_consolidation']
p_a_b = (df[(df.fico>700) & (df.purpose == 'debt_consolidation')].shape[0]/df.shape[0])/p_b
print(f'p_a_b:{p_a_b}')
result = (p_a_b == p_a)
print(f'Results: {result}')
# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
print(f'prpb_lp: {prob_lp}')
prob_cs = df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
print(f'prob_cs: {prob_cs}')
new_df = df[df['paid.back.loan']=='Yes']
bayes = (new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0])*prob_lp/prob_cs
#print(f'prob_pd_c:{prob_pd_cs}')
prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
#print(f'Bayes: {bayes}')
# code ends here


# --------------
# code starts here
xdf = df['purpose'].value_counts()
plt.figure(figsize = (15,5))
plt.bar(xdf.index, xdf)
plt.show()
df1 = df[df['paid.back.loan']=='No']
kdf = df1['purpose'].value_counts()
plt.figure(figsize = (15,5))
plt.bar(kdf.index, kdf)
plt.show()
# code ends here


# --------------

# Calculate median 
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()


# histogram for installment
df['installment'].hist(normed = True, bins=50)
plt.axvline(x=inst_median,color='r')
plt.axvline(x=inst_mean,color='g')

plt.show()

#histogram for log anual income
df['log.annual.inc'].hist(normed = True, bins=50)
plt.show()


