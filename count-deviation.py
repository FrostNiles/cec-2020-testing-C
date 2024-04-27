import numpy as np

newNumbers ="3.79968029810100733e+01   5.22677018364275303e+01   6.32647648375782943e+01  -6.90973748215927623e+01  -3.95786265095596293e+01  -7.79757461687436933e+01   2.16341419246206743e+01  -7.49766729003641183e+01   2.70585635802981233e+01   5.327809407062723e+01"
oldNumbers ="3.7996802981010077e+01   5.2267701836427534e+01   6.3264764837578298e+01  -6.9097374821592766e+01  -3.9578626509559633e+01  -7.7975746168743697e+01   2.1634141924620678e+01  -7.4976672900364122e+01   2.7058563580298127e+01   5.3278094070627390e+01"

newNumbers = [float(i) for i in newNumbers.split()]
oldNumbers = [float(i) for i in oldNumbers.split()]

deviations = [abs(old - new) for old, new in zip(oldNumbers, newNumbers)]

average_deviation = sum(deviations) / len(deviations)
print("Average deviation: ", average_deviation)

median_deviation = np.median(deviations)

print("Median deviation: ", median_deviation)
