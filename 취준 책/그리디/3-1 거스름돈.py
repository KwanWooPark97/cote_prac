import time
start_time=time.time()
N=1260

five=int(N/500)
print(five)
hund=int((N-500*five)/100)
print(hund)
fifty=int((N-500*five-100*hund)/50)
print(fifty)
ten=int((N-500*five-100*hund-50*fifty)/10)
print(ten)
coin=five+hund+fifty+ten

end_time=time.time()

fps=end_time-start_time

print(coin,fps)

#책의 정답

N=1260
count=0

coin_type=[500,100,50,10]

for i in coin_type:
    count += N//i
    N %= i

print(count)