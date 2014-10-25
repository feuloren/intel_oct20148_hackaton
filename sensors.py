import pyupm_grove as grove

light = grove.GroveLight(0) # Analog port number
print light.raw_value() # raw value given by sensor
print light.value() # value converted in Lux (I guess)

