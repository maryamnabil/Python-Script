import csv
myDict1 = {}
i = 0
name = "name"
Email = "Email"
mobile = "mobile"
University = "University"
Major = "Major"
f = open("out.csv", "w")
f.truncate()
f.close()

while True:
    myDict1[name] = raw_input("Please Enter Your Name")
    myDict1[Email] = raw_input("Please Enter your Email")
    myDict1[mobile] = raw_input("Please Enter your Mobile")
    myDict1[University] = raw_input("Please Enter your University")
    myDict1[Major] = raw_input("Please Enter your Major")
    #print (myDict1)
    with open('out.csv', 'a') as f:
        i += 1
        w = csv.DictWriter(f, myDict1.keys())
        if i == 1:
            w.writeheader()
            w.writerow(myDict1)
        else:
            w.writerow(myDict1)
    stop = raw_input('For Another input Press Enter , To stop Type Stop')
    if stop == "Stop":
        print ('Thank You for Entering ^_^ ')
        break
    else:
        pass




