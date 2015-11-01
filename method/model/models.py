# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.
# Basic model functions.  Should be applicable to any case where there is f(x) = y.

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def linear(x, y):
    regression = LinearRegression()
    regression.fit(x, y)
    return regression.predict(x)

def quadratic(x, y):
    poly = PolynomialFeatures(degree=2)
    polinomial_x = PolynomialFeatures(degree=2).fit_transform(x)
    regression = LinearRegression()
    regression.fit(polinomial_x, y)
    return regression.predict(polinomial_x)
