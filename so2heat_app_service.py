from so2heat_response import SO2HeatResponse
from soheat_response_command import SO2HeatResponseCommand

response = SO2HeatResponse()
response.commands.append(SO2HeatResponseCommand("photo", []))
response.commands.append(SO2HeatResponseCommand("nextTimeout", [1000]))

json = response.serialize()
print(json)

obj = response.deserialize(json)
print(obj)

