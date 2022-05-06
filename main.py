# Import Genie
from genie import testbed
import pprint


print("asd")

testbed = testbed.load('devices.yaml')
device = testbed.devices['asw01']
device.connect()
output = device.parse('show dot1x all')

pprint.pprint(output)


print("Good bye!")