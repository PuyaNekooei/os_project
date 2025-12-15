import threading ,time,random

M = random.randint(1, 5)   # washers
D = random.randint(1, 3)   # dryers
C = random.randint(3, 50)  # customers

print(f"{M} washers, {D} dryers, {C} customers\n")


washers=threading.Semaphore(M)
dryers=threading.Semaphore(D)


def customer(id):

    print(f"customer {id} request for washers ")
    washers.acquire()
    print(f"customer {id} get washers ")
    wash_time = random.randint(2,5)
    time.sleep(wash_time)
    washers.release()

    print(f"customer {id} request for dryers ")
    dryers.acquire()
    print(f"customer {id} get dryers ")
    dryers_time = random.randint(1,3)
    time.sleep(dryers_time)
    dryers.release()

    print(f"customer {id} done")


threads=[]

for i in range (1,C+1):
    t = threading.Thread(target=customer, args=(i,))
    threads.append(t)

    t.start()

    time.sleep(random.randint(1, 4))

for t in threads:
    t.join()

print(f"all customers finished")



