
import time

def main():
    inicio = time.time()

    list1 = []
    for a in range(1000):
        for b in range(1000):
            list1.append(a)
    
    fin = time.time()
    print(fin-inicio)

if __name__ == "__main__":
    main()