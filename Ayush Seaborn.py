import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#=[1,2,3,4,5]
#[10,20,15,25,30]
#ns.lineplot(x=x,y=y)
#lt.show()

df=pd.DataFrame({
    "student":["Aman","Riya","Karan","Neha"],
    "Marks":[85,92,78,88]
})
sns.barplot(data=df,x="student",y="Marks")
plt.show()