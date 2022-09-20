#!/usr/bin/env python3


proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

print(proto)
proto.append("dns") # this line will add "dns" to the end of our list

protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports

proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)

protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

pop_proto = proto.pop(0) # remove the "ssh" from proto list and return 
print(pop_proto)
print(proto)


proto3 = [ 22, 22, 35, 13, 22, 34, 145]

proto3_count = proto3.count(22) # return the number of times number 22 appears in the proto3 list 
print(proto3_count)

proto3_reverse = proto3.reverse() # reverse the elementes of the proto3
print(proto3)


