#rating stats
import pandas

file=pandas.read_csv("rating.csv")
file.describe()
"""
            user_id     sofifa_id        rating
count  2.418808e+07  2.418808e+07  2.418808e+07
mean   6.923914e+04  2.172752e+05  2.797685e+00
std    3.997268e+04  3.322979e+04  9.208580e-01
min    1.000000e+00  4.100000e+01  1.000000e+00
25%    3.462300e+04  1.980090e+05  2.000000e+00
50%    6.924000e+04  2.233130e+05  2.500000e+00
75%    1.038390e+05  2.431700e+05  3.500000e+00
max    1.384930e+05  2.589700e+05  5.000000e+00
"""

file.nunique()
user_id      138493
sofifa_id     18929
rating            9
dtype: int64


import pandas

file=pandas.read_csv("tags.csv")
user_id      68632
sofifa_id    18944
tag            936
