import hashlib
import timeit

if __name__ == '__main__':
    text=open("text.txt").read()
    start=timeit.default_timer()
    m=hashlib.md5("abc".encode('utf-8'))
    print(m.hexdigest())
    end=timeit.default_timer()
    print('md5 \ntime: ' + str(format((end-start), '.20f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size) +'\n')

    start = timeit.default_timer()
    m = hashlib.sha1(text.encode('utf-8'))
    print(m.hexdigest())
    end = timeit.default_timer()
    print('sha1 \ntime: ' + str(format((end-start), '.10f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = timeit.default_timer()
    m = hashlib.sha224(text.encode('utf-8'))
    print(m.hexdigest())
    end = timeit.default_timer()
    print('sha224 \ntime: ' + str(format((end-start), '.10f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = timeit.default_timer()
    m = hashlib.sha256(text.encode('utf-8'))
    print(m.hexdigest())
    end = timeit.default_timer()
    print('sha256 \ntime: ' + str(format((end-start), '.10f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = timeit.default_timer()
    m = hashlib.sha384(text.encode('utf-8'))
    print(m.hexdigest())
    end = timeit.default_timer()
    print('sha384 \ntime: ' + str(format((end-start), '.10f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = timeit.default_timer()
    m = hashlib.sha512(text.encode('utf-8'))
    print(m.hexdigest())
    end = timeit.default_timer()
    print('sha512 \ntime: ' + str(format((end-start), '.10f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = timeit.default_timer()
    m = hashlib.sha3_224(text.encode('utf-8'))
    print(m.hexdigest())
    end = timeit.default_timer()
    print('sha3_224 \ntime: ' + str(format((end-start), '.10f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = timeit.default_timer()
    m = hashlib.sha3_256(text.encode('utf-8'))
    print(m.hexdigest())
    end = timeit.default_timer()
    print('sha3_256 \ntime: ' + str(format((end-start), '.10f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = timeit.default_timer()
    m = hashlib.sha3_384(text.encode('utf-8'))
    print(m.hexdigest())
    end = timeit.default_timer()
    print('sha3_384 \ntime: ' +str(format((end-start), '.10f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = timeit.default_timer()
    m = hashlib.sha3_512(text.encode('utf-8'))
    print(m.hexdigest())
    end = timeit.default_timer()
    print('sha3_512 \ntime: ' + str(format((end-start), '.10f')) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')