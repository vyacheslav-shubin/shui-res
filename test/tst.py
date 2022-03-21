import re
row="ok T0:24.00 /0.00 B:84.09 /70.00 T0:24.00 /0.00 T1:116.75 /0.00 @:0 B@:0 @0:0 @1:0"
match = re.search(r'T0\:(\d+\.\d+)\s*\/(\d+\.\d+)\s*B\:(\d+\.\d+)\s*\/(\d+\.\d+)', row)
if match:
    print(match[1])
    print(match[2])
    print(match[3])
    print(match[4])

