from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    results = p.imap(f,range(300))
    for item in results:
        print(item)
    p.close()