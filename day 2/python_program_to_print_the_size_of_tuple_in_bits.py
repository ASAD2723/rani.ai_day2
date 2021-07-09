import sys

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("asad", "vinay", "azaz", "sachin", "ayush", "gaurav")
Tuple3 = ((1, "golden"), ( 2, "orange"), (3, "red"), (4, "captain"))

print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")