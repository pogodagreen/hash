import hashlib
import time

if __name__ == '__main__':
    text="abc"

    start=time.time()
    m=hashlib.md5("abc".encode('utf-8'))
    print(m.hexdigest())
    end=time.time()
    print('md5 \ntime: ' + str(end-start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size) +'\n')

    start = time.time()
    m = hashlib.sha1(text.encode('utf-8'))
    print(m.hexdigest())
    end = time.time()
    print('sha1 \ntime: ' + str(end - start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = time.time()
    m = hashlib.sha224(text.encode('utf-8'))
    print(m.hexdigest())
    end = time.time()
    print('sha224 \ntime: ' + str(end - start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = time.time()
    m = hashlib.sha256(text.encode('utf-8'))
    print(m.hexdigest())
    end = time.time()
    print('sha256 \ntime: ' + str(end - start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = time.time()
    m = hashlib.sha384(text.encode('utf-8'))
    print(m.hexdigest())
    end = time.time()
    print('sha384 \ntime: ' + str(end - start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = time.time()
    m = hashlib.sha512(text.encode('utf-8'))
    print(m.hexdigest())
    end = time.time()
    print('sha512 \ntime: ' + str(end - start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = time.time()
    m = hashlib.sha3_224(text.encode('utf-8'))
    print(m.hexdigest())
    end = time.time()
    print('sha3_224 \ntime: ' + str(end - start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = time.time()
    m = hashlib.sha3_256(text.encode('utf-8'))
    print(m.hexdigest())
    end = time.time()
    print('sha3_256 \ntime: ' + str(end - start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = time.time()
    m = hashlib.sha3_384(text.encode('utf-8'))
    print(m.hexdigest())
    end = time.time()
    print('sha3_384 \ntime: ' + str(end - start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')

    start = time.time()
    m = hashlib.sha3_512(text.encode('utf-8'))
    print(m.hexdigest())
    end = time.time()
    print('sha3_512 \ntime: ' + str(end - start) + '\ndigest size: ' + str(m.digest_size) + '\nblock size: ' + str(m.block_size)+'\n')