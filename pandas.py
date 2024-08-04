import numpy as np
import pandas as np

#a)Creating dataframe from a dictionary of ndarray/lists
lst=['welcome','to','cvr','college','of','enginerring']
#             0
# 0      welcome
# 1           to
# 2          cvr
# 3      college
# 4           of
# 5  enginerring
# <class 'pandas.core.frame.DataFrame'>
print(type(pd.DataFrame(lst)))
print(pd.DataFrame(lst))
lst=[['vignay','C4'],['Revanth','C3'],['Vaishnav','C5']]
print(lst)
# [['vignay', 'C4'], ['Revanth', 'C3'], ['Vaishnav', 'C5']]
#           0   1
# 0    vignay  C4
# 1   Revanth  C3
# 2  Vaishnav  C5
print(pd.DataFrame(lst))
data={'Name':["vignay","varun","revanth","vaishnav"],'Age':[18,19,20,21]}
# {'Name': ['vignay', 'varun', 'revanth', 'vaishnav'], 'Age': [18, 19, 20, 21]}
#        Name  Age
# 0    vignay   18
# 1     varun   19
# 2   revanth   20
# 3  vaishnav   21
print(data)
print(pd.DataFrame(data))
data={'Name':["vignay","varun","revanth","vaishnav"],
      'Age':[18,19,20,21],
      'Address':["usa","uk","canada","india"],
      'Qualifications':['M.S',"Btech","C.A","M.B.B.S"]}
#        Name  Age Address Qualifications
# 0    vignay   18     usa            M.S
# 1     varun   19      uk          Btech
# 2   revanth   20  canada            C.A
# 3  vaishnav   21   india        M.B.B.S
a=pd.DataFrame(data)
#        Name Qualifications
# 0    vignay            M.S
# 1     varun          Btech
# 2   revanth            C.A
# 3  vaishnav        M.B.B.S
b=a[['Name','Qualifications']]
print(b)
#b)Slicing in dataframes using Iloc and Loc   (location and indexlocation)---------------------------------------------------------
data={'one':pd.Series([1,2,3,4]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000])
      }
#    one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
a=pd.DataFrame(data)
#    one  two  three  four
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a.loc[1:])
#   one  two  three  four
# 3    4   40    400  4000
# 2    3   30    300  3000
# 1    2   20    200  2000
# 0    1   10    100  1000
print(a.loc[::-1])
# print(a.loc[1:-1])#error
#    two  three  four
# 1   20    200  2000
# 2   30    300  3000
# Last element is included in the loc whereas iloc performs normal slicing-------------------------------------------------------------------------------------------------------------------------------------------
print(a.loc[1:2,'two':'four'])
print("*"*100)
# ****************************************************************************************************
#    one  two  three  four
# 1    2   20    200  2000
print(a.iloc[1:2])
#   one  two  three  four
# 0    1   10    10--------------------------------------------------------------0  1000
print(a.iloc[1:-1,:])
   # one  two  three  four
# 1    2   20    200  2000
# 2    3   30    300  3000
# -------------------------------------------------------------------------
#    two  three
# 1   20    200
# 2   30    300
print(a.iloc[1:-1,1:-1])
#    three
# 0    100
# 1    200
# 2    300
# 3    400
print(a.iloc[:,2:3])
#    one  two  three  four
# 0    1   10    100  1000
# 2    3   30    300  3000
print(a.iloc[[0,2]])
#Select in specific rows
#    two  four
# 0   10  1000
# 2   30  3000
print(a.iloc[[0,2],[1,3]])
#c)Slicing Using Conditions
# 0    False
# 1    False
# 2     True
# 3     True
# Name: two, dtype: bool
print(a['two']>20)
#    one  two  three  four
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a[a['two']>20])
c=a.loc[a['two']>20,["three","four"]]
#    three  four
# 2    300  3000
# 3    400  4000
print(c)
# f1=open("file1.txt","r")
# f2=open("file2.txt","r")
# f11=f1.read()
# f22=f2.read()
# temp=f11
print(a.loc[a['three']<300,['one','four']])
#c)Column addition in DataFrame
#    one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a)
l=[22,33,44,55]
#    one  two  three  four  five
# 0    1   10    100  1000    22
# 1    2   20    200  2000    33
# 2    3   30    300  3000    44
# 3    4   40    400  4000    55
a['five']=l
print(a)
l1=pd.Series([111,222,333,444])
#    one  two  three  four  five  six
# 0    1   10    100  1000    22  111
# 1    2   20    200  2000    33  222
# 2    3   30    300  3000    44  333
# 3    4   40    400  4000    55  444
a['six']=l1
print(a)
# 0    11
# 1    12
# 2    13
# 3    14
# Name: one, dtype: int64
a['seven']=a['one']+10
#    one  two  three  four  five  six  seven
# 0    1   10    100  1000    22  111     11
# 1    2   20    200  2000    33  222     12
# 2    3   30    300  3000    44  333     13
# 3    4   40    400  4000    55  444     14
print(a)
#   one  two  three  four  five  six  seven  eight
# 0    1   10    100  1000    22  111     11    0.1
# 1    2   20    200  2000    33  222     12    0.2
# 2    3   30    300  3000    44  333     13    0.3
# 3    4   40    400  4000    55  444     14    0.4
a['eight']=a['one']/10
print(a)
#d)Column deletion in DataFrames
#USING del
#USING pop
del a['eight']
#    one  two  three  four  five  six  seven
# 0    1   10    100  1000    22  111     11
# 1    2   20    200  2000    33  222     12
# 2    3   30    300  3000    44  333     13
# 3    4   40    400  4000    55  444     14
print(a)
# 0    11
# 1    12
# 2    13
# 3    14
# Name: seven, dtype: int64
print(a.pop('seven'))
#    one  two  three  four  five  six
# 0    1   10    100  1000    22  111
# 1    2   20    200  2000    33  222
# 2    3   30    300  3000    44  333
# 3    4   40    400  4000    55  444
print(a)
#e)Addition of rows
d1=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
d2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
#    a  b
# 0  1  2
# 1  3  4
print(d1)
#    a  b
# 0  5  6
# 1  7  8
print(d2)
#    a  b
# 0  1  2
# 1  3  4
# 0  5  6
# 1  7  8
#append
print(d1._append(d2).reset_index(drop=True))
#    a  b
# 0  1  2
# 1  3  4
# 2  5  6
# 3  7  8
#f)Pandas drop function
data={'one':pd.Series([1,2,3,4]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000])
      }
#    one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
a=pd.DataFrame(data)
print(a)
# axis=0-->row wise--------------------------------------------------------------------------------------------------------------
# axis=1-->column wise-----------------------------------------------------------------------------------------------------------
#   one  two  three  four
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a.drop([0,1],axis=0))
# d=a.drop([0,1],inplace=True)-------------------------
#     two  four
# 0   10  1000
# 1   20  2000
# 2   30  3000
# 3   40  4000
print(a.drop(['one','three'],axis=1))
#   one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a)
c=a.drop(['one','three'],axis=1,inplace=True)#-----------------
#    two  four
# 0   10  1000
# 1   20  2000
# 2   30  3000
# 3   40  4000
print(a)
#g)Transposing a DataFrame
data={'one':pd.Series([1,2,3,4]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000])
      }
a=pd.DataFrame(data)
#    one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a)
b=a.T
#          0     1     2     3
# one       1     2     3     4
# two      10    20    30    40
# three   100   200   300   400
# four   1000  2000  3000  4000
print(b)
#h)A set of more DataFrame Functionalities
#1)Axis
#    one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a.axes)
# [RangeIndex(start=0, stop=4, step=1), Index(['one', 'two', 'three', 'four'], dtype='object')]
#2)ndim function
# 2------for a data frame-always (rows and columns)
print(a.ndim)
# 3)dtypes function
# one      int64
# two      int64
# three    int64
# four     int64
# dtype: object
print(a.dtypes)
#4)shape function
print(a.shape)
# (4, 4)
#5)head() function
d={'name':pd.Series(["tom","jerrry",'olive','spike','popey','mickey','bluto']),
   'age':pd.Series([10,12,14,30,28,33,15]),
   'Height':pd.Series([3.25,1.11,4.12,5.47,6.15,6.67,2.61])
   }
a=pd.DataFrame(d)
#     name  age  Height
# 0     tom   10    3.25
# 1  jerrry   12    1.11
# 2   olive   14    4.12
# 3   spike   30    5.47
# 4   popey   28    6.15
# 5  mickey   33    6.67
# 6   bluto   15    2.61
print(a)
#This head() method returns first n rows (by default=5) of the dataframe
#     name  age  Height
# 0     tom   10    3.25
# 1  jerrry   12    1.11
# 2   olive   14    4.12
# 3   spike   30    5.47
# 4   popey   28    6.15
print(a.head())
#      name  age  Height
# 0     tom   10    3.25
# 1  jerrry   12    1.11
# 2   olive   14    4.12
print(a.head(3))
#No error when more number is given all are printed-------------------------------------------------
#6)Tail() function
print(a.tail())
#      name  age  Height
# 2   olive   14    4.12
# 3   spike   30    5.47
# 4   popey   28    6.15
# 5  mickey   33    6.67
# 6   bluto   15    2.61
#Prints last five values by default similar to head()
#7)empty function
#Tells whether dataframe is empty or not
# False
print(a.empty)
df=pd.DataFrame([])#()
# True
print(df.empty)
#i)Statistical or Mathematical Functions
data={'one':pd.Series([1,2,3,4]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000])
      }
a=pd.DataFrame(data)
#    one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a)
# one         10
# two        100
# three     1000
# four     10000
# dtype: int64
#a)sum()
print(a.sum())
# one         2.5
# two        25.0
# three     250.0
# four     2500.0
# dtype: float64
#b)mean()
print(a.mean())
# one         2.5
# two        25.0
# three     250.0
# four     2500.0
# dtype: float64
#c)median()
print(a.median())
#d)mode()
d=pd.DataFrame({'A':[1,2,2,3,4,4,4,5],
                'B':[10,20,20,30,40,40,50,60]}
               )
print(d)
#    A   B
# 0  1  10
# 1  2  20
# 2  2  20
# 3  3  30
# 4  4  40
# 5  4  40
# 6  4  50
# 7  5  60
# ----------------------------------------------------
# 0    4
# Name: A, dtype: int64
print(d['A'].mode())
print(d['B'].mode())
# 0    4
# Name: A, dtype: int64
# 0    20
# 1    40
# Name: B, dtype: int64
#e)variance()
# A      1.839286
# B    283.928571
# dtype: float64
print(d.var())
#f)min() function
# A     1
# B    10
# dtype: int64
print(d.min())
# #g)max() function
# A     5
# B    60
# dtype: int64
print(d.max())
#h)Standard Deviation() function
# A     1.356203
# B    16.850180
# dtype: float64
print(d.std())
#j)Describe Function
data={'one':pd.Series([1,2,3,4]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000]),
      'five':pd.Series(['A','B','C','D'])
      }
a=pd.DataFrame(data)
#             one        two       three         four
# count  4.000000   4.000000    4.000000     4.000000
# mean   2.500000  25.000000  250.000000  2500.000000
# std    1.290994  12.909944  129.099445  1290.994449
# min    1.000000  10.000000  100.000000  1000.000000
# 25%    1.750000  17.500000  175.000000  1750.000000
# 50%    2.500000  25.000000  250.000000  2500.000000
# 75%    3.250000  32.500000  325.000000  3250.000000
# max    4.000000  40.000000  400.000000  4000.000000
print(a.describe())
#K)Pipe function
#1)Pipe Function
data={'one':pd.Series([1,2,3,4]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000])
      }
a=pd.DataFrame(data)
#Allows a specific function for whole like apply()------------------
#    one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a)
def  add(i,j):
    return i+j
def sub(i,j):
    return i-j
#    one  two  three  four
# 0   11   20    110  1010
# 1   12   30    210  2010
# 2   13   40    310  3010
# 3   14   50    410  4010
print(a.pipe(add,10))
def mean(col):
    return col.mean()
def square(i):
    return i**2
# one         2.5
# two        25.0
# three     250.0
# four     2500.0
# dtype: float64
print(a.pipe(mean))
#    one   two   three      four
# 0    1   100   10000   1000000
# 1    4   400   40000   4000000
# 2    9   900   90000   9000000
# 3   16  1600  160000  16000000
print(a.pipe(square))
# one            6.25
# two          625.00
# three      62500.00
# four     6250000.00
# dtype: float64
print(a.pipe(mean).pipe(square))
#2)Apply Function
data={'one':pd.Series([1,2,3,4]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000])
      }
a=pd.DataFrame(data)
print(a)
#apply a function to dataframe either whole or a single element
# one         2.5
# two        25.0
# three     250.0
# four     2500.0
# dtype: float64
print(a.apply(np.mean))
#    one   two   three      four
# 0    1   100   10000   1000000
# 1    4   400   40000   4000000
# 2    9   900   90000   9000000
# 3   16  1600  160000  16000000
print(a.apply(square))
# one         3
# two        30
# three     300
# four     3000
# dtype: int64
print(a.apply(lambda x:x.max()-x.min()))
#3)Apply map or map function
#Applymap has beeen deprecated from  the python ----------------
#    one   two  three    four
# 0  100  1000  10000  100000
# 1  200  2000  20000  200000
# 2  300  3000  30000  300000
# 3  400  4000  40000  400000
print(a.map(lambda x:x*100))
#Element wise operation only
a=pd.DataFrame({'A':[1.2,3.4,5.6],
                'B':[7.8,9.1,2.3]})
#      A    B
# 0  1.2  7.8
# 1  3.4  9.1
# 2  5.6  2.3
print(a)
#    A  B
# 0  1  7
# 1  3  9
# 2  5  2
b=a.map(np.int64)
print(b)
# print(b.map(lambda row:row.mean(),axis=1))------------------#ERROR--------------------
c=a.apply(lambda row:row.mean(),axis=1)
# 0    4.50
# 1    6.25
# 2    3.95
# dtype: float64
print(c)
#l)Reindex Function
data={'one':pd.Series([1,2,3,4]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000])
      }
a=pd.DataFrame(data)
print(a)
print("*"*700)
#    one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
#*************************************************
#ROWS REINDEXING
#    one  two  three  four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
b=a.reindex([0,1,2,3])
print(b)
#COLUMN REINDEXING
data={'Name':['John','Jane','Jim','Joan'],
      'Age':[25,30,35,40],
      'City':['New York','Los Angeles','Chicago','Houston']}
a=pd.DataFrame(data)
#   Name         City  Age
# 0  John     New York   25
# 1  Jane  Los Angeles   30
# 2   Jim      Chicago   35
# 3  Joan      Houston   40
c=a.reindex(index=[0,1,2,3],columns=["Name",'City',"Age"])
print(c)
#We can't change the index but we can change the referringindex-----------
#m)Renaming Columns in pandas DataFrame
data={'one':pd.Series([1,2,3,4]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000])
      }
a=pd.DataFrame(data)
#   One  Two  Three  Four
# 0    1   10    100  1000
# 1    2   20    200  2000
# 2    3   30    300  3000
# 3    4   40    400  4000
print(a.rename(columns={'one':'One','two':'Two',"three":"Three",'four':"Four"}))
#Inplace make the data change in original dataframes-------------------------------------------------
#    One  Two  Three  Four
# a    1   10    100  1000
# b    2   20    200  2000
# c    3   30    300  3000
# d    4   40    400  4000
print(a.rename(columns={'one':'One','two':'Two',"three":"Three",'four':"Four"},index={0:'a',1:'b',2:'c',3:'d'}))
a.rename(columns={'one':'One','two':'Two',"three":"Three",'four':"Four"},inplace=True,index={0:'a',1:'b',2:'c',3:'d'})
print(a)
#inplace returns  none
#n)Sorting in Pandas DataFrames
data={'one':pd.Series([111,21,31,41]),
      'two':pd.Series([10,20,30,40]),
      'three':pd.Series([100,200,300,400]),
      'four':pd.Series([1000,2000,3000,4000])
      }
a=pd.DataFrame(data)
#Sort with respect to specified column
#    one  two  three  four
# 1   21   20    200  2000
# 2   31   30    300  3000
# 3   41   40    400  4000
# 0  111   10    100  1000
print(a.sort_values(by="one"))
#Sort in specific value
#    one  two  three  four
# 0  111   10    100  1000
# 3   41   40    400  4000
# 2   31   30    300  3000
# 1   21   20    200  2000
print(a.sort_values(by="one",ascending=False))
#Sort in specific Order on multiple Columns
#    one  two  three  four
# 1   21   20    200  2000
# 2   31   30    300  3000
# 3   41   40    400  4000
# 0  111   10    100  1000
print(a.sort_values(by=['one','two']))
#Sort with specific Sorting Algorithm<br>
#Quicksort,Mergesort,Heapsort
#    one  two  three  four
# 1   21   20    200  2000
# 2   31   30    300  3000
# 3   41   40    400  4000
# 0  111   10    100  1000
print(a.sort_values(by=['one'],kind="heapsort"))
#o)Groupby functions
cricket={"Team":['India','India','Australia','Australia','SA','SA','SA','SA','NZ','NZ','NZ','India'],
         "Rank":[2,3,4,2,3,4,1,1,2,4,1,2],
         "Year":[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         "Points":[876,801,891,815,776,784,834,824,758,691,883,782]
         }
#         Team  Rank  Year  Points
# 0       India     2  2014     876
# 1       India     3  2015     801
# 2   Australia     4  2014     891
# 3   Australia     2  2015     815
# 4          SA     3  2014     776
# 5          SA     4  2015     784
# 6          SA     1  2016     834
# 7          SA     1  2017     824
# 8          NZ     2  2016     758
# 9          NZ     4  2014     691
# 10         NZ     1  2015     883
# 11      India     2  2017     782
a=pd.DataFrame(cricket)
print(a)

# print("*"*200)
#****************************************************---Important one
print(a.groupby('Team'))
#<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001970F37CD40>
print(a.groupby('Team').groups)
# {'Australia': [2, 3], 'India': [0, 1, 11], 'NZ': [8, 9, 10], 'SA': [4, 5, 6, 7]}
#To serch for specific Country with specific year
print(a.groupby(['Team','Year']).get_group(('Australia',2014)))
#         Team  Rank  Year  Points
# 2  Australia     4  2014     891
#If data is not present then we get an error
#     raise KeyError(gpr)
# KeyError: 'USA'
# print(a.groupby(['USA']))
#Adding statistical Computation on top of groupby
print(a.groupby('Team')['Points'].sum()) #or
print(a.groupby('Team').sum()['Points'])
# Team
# Australia    1706
# India        2459
# NZ           2332
# SA           3218
# Name: Points, dtype: int64
# Team
# Australia    1706
# NZ           2332
# India        2459
# SA           3218
# Name: Points, dtype: int64
print(a.groupby('Team').sum()['Points'].sort_values())#ascending=False
#Checking multiple stats for points team wise
groups=a.groupby('Team')
#<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000283DF9C76E0>
print(groups)
# Team
# Australia    1706
# India        2459
# NZ           2332
# SA           3218
# Name: Points, dtype: int64
print(groups['Points'].sum())
#             sum        mean        std  max  min
# Team
# Australia  1706  853.000000  53.740115  891  815
# India      2459  819.666667  49.702448  876  782
# NZ         2332  777.333333  97.449132  883  691
# SA         3218  804.500000  28.769196  834  776
result = groups['Points'].agg(["sum","mean","std","max","min"])
print(result)
#Filter function along with groupby
#   Team  Rank  Year  Points
# 4   SA     3  2014     776
# 5   SA     4  2015     784
# 6   SA     1  2016     834
# 7   SA     1  2017     824
print(a.groupby('Team').filter(lambda x:len(x)==4))
#      Team  Rank  Year  Points
# 0   India     2  2014     876
# 1   India     3  2015     801
# 8      NZ     2  2016     758
# 9      NZ     4  2014     691
# 10     NZ     1  2015     883
# 11  India     2  2017     782
print(a.groupby('Team').filter(lambda x:len(x)==3))
                                                                         #3)Working with csv files and basic data analysis using Pandas
#a)Reading csv
a=pd.read_csv('Football.csv')#Or the link
print(a)
print(a.head())#Print 5 lines (first by default)
#b)Pandas Info Function
print(a.info())
#c)isnull() function to check if there are any nan values
print(a.isnull())#GIVES TRUE OR FALSE in all rows and columns
print(a.isnull().sum())#Gives the sum values of all rows which are emty or not
#d)Quantile function to get the specific percentile value
print(a.describe(percentiles=[.00]))#Gives count,mean,std,50%,80%,max
#Let us use the quantile function to get the exact value now
print(a['Mins'].quantile(.80))

