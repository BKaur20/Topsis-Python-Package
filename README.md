# Topsis-Python-Package
A Multiple Criteria Decision Making Module called TOPSIS.

# Assignment 1:

# What is Topsis:
Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) originated in the 1980s as a multi-criteria decision making method. TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution, and greatest distance from the negative-ideal solution.

# How to use this package:
TOPSIS-102017051 can be run as follows:

# CLI:
topsis 102017051-data.csv "1,1,1,1,1" "+,-,+,-,+" 102017051-result1.csv

# Sample dataset
The decision matrix should be constructed with each row representing a Model alternative, and each column representing a criterion like Accuracy, R2, Root Mean Squared Error, Correlation, and many more.
Weights are not already normalised will be normalised later in the code.
Information of positive(+) or negative(-) impact criteria should be provided in I.

# Output
The rankings are displayed , with the 1st rank offering us the best decision, and last rank offering the worst decision making, according to TOPSIS method.
