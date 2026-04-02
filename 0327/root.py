count = 100
start = 1.0
end = 2.0

for i in range(count):
    x = start + i*((end-start)/count)
    f = (x**2 -x -1)
    if abs(f-0.0) < 0.01 :
        print("방정식의 해는 ", x)