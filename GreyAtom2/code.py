# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter = ",", skip_header = 1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
census = np.concatenate((data,new_record))


# --------------
#Code starts here
age = census[:,0]
max_age = age.max()
print("max_age",max_age)
min_age = age.min()
print("min age",min_age)
age_mean = age.sum()/age.size
print("mean_age",age_mean)
age_std = np.std(age)
print("std", age_std)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
array = [len_0, len_1, len_2, len_3, len_4]
minority_race = array.index(min(array))
print("Race",minority_race,"is the minority")



# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()
print("Income of highly educated people", avg_pay_high)
print("Income of less educated people",avg_pay_low)


