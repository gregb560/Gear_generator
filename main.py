import numpy as np
import math as mt
from matplotlib import pyplot as plt
import xlsxwriter
import wzory
import dane
print(dane.i)
print(dane.z1)
print(dane.m)
z2 = wzory.Gear_teeth_number(dane.i,dane.z1)

print (z2)

gear1 = wzory.Gear_wheel_parameters(dane.m,dane.z1,0,0,dane.alfa)
print()
gear2 = wzory.Gear_wheel_parameters(dane.m,z2,0,0,dane.alfa)
print()
print(gear1)
print()
print(gear2)




data = [
    {
        "Przelozenie calkowite": dane.i,
        "Modul" : dane.m,
        "Liczba zebow" : dane.z1,
        "ha": gear1[0],
        "d": gear1[1],
        "da": gear1[2],
        "dax": gear1[3],
        "hf": gear1[4],
        "df": gear1[5],
        "dfx": gear1[6],
        "db": gear1[7],
        "alfa_0": dane.alfa

    },
    {
        "Przelozenie calkowite": dane.i,
        "Modul": dane.m,
        "Liczba zebow": z2,
        "ha": gear2[0],
        "d": gear2[1],
        "da": gear2[2],
        "dax": gear2[3],
        "hf": gear2[4],
        "df": gear2[5],
        "dfx": gear2[6],
        "db": gear2[7],
        "alfa_0": dane.alfa

    }
]
workbook = xlsxwriter.Workbook("Gear_parameter.xlsx")
worksheet = workbook.add_worksheet("firstSheet")
worksheet.write(0,0,"Gear")
worksheet.write(0,1,"Przelozenie calkowite")
worksheet.write(0,2,"Modul")
worksheet.write(0,3,"Liczba zebow")
worksheet.write(0,4,"ha")
worksheet.write(0,5,"d")
worksheet.write(0,6,"da ")
worksheet.write(0,7,"dax")
worksheet.write(0,8,"hf")
worksheet.write(0,9,"df")
worksheet.write(0,10,"dfx")
worksheet.write(0,11,"db")
worksheet.write(0,12,"alfa_0")

for index, entry, in enumerate(data):
    worksheet.write(index + 1, 0, str(index+1))
    worksheet.write(index + 1, 1, entry["Przelozenie calkowite"])
    worksheet.write(index + 1, 2, entry["Modul"])
    worksheet.write(index + 1, 3, entry["Liczba zebow"])
    worksheet.write(index + 1, 4, entry["ha"])
    worksheet.write(index + 1, 5, entry["d"])
    worksheet.write(index + 1, 6, entry["da"])
    worksheet.write(index + 1, 7, entry["dax"])
    worksheet.write(index + 1, 8, entry["hf"])
    worksheet.write(index + 1, 9, entry["df"])
    worksheet.write(index + 1, 10, entry["dfx"])
    worksheet.write(index + 1, 11, entry["db"])
    worksheet.write(index + 1, 12, entry["alfa_0"])

workbook.close()


