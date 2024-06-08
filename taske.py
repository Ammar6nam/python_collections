temperatureInCelisus=[20.5,22.4,19.8,21.3,18.9]
pollution=["CO2", "Ozone", "CO2", "SO2", "CO2"]
airQualityIndex=[45,62,150,55,112]
humidityLevel=[45,55,60,48,53]

# def tempConversion(args):
#     result=[]
#     for i in args:
#         x=(cel*9/5)+32
#         result.append(x)
#     return result
# tempConversion(temperatureInCelisus,humidityLevel)

# def convert(arr):
#     return [(cel*9/5)+32 for cel in arr]
# print(convert(temperatureInCelisus))

# tempFahrenheit=[*map(lambda cel:(cel*9/5)+32,temperatureInCelisus)]
# print(tempFahrenheit)

# def poorAir(quality):
#     result=[]
#     for qual in quality:
#         if qual >100:
#             result.append(qual)
#             return result
# print(poorAir(airQualityIndex))

# def airPoor(args):
#     return[arg for arg in args if arg > 100]
# airPoor(airQualityIndex)

# poorAirQual=list(filter(lambda x : x>100,airQualityIndex))
# print(poorAirQual)

f = open('./python/collection/text1x.py','x')
w = open('.python/collection/text2w.py','w')
a = open('./python/collection/text3a.py','a')