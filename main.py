import time

def task_1():
    print('Task 1 started')
    time.sleep(2)
    print('Task 1 completed')

def task_2():
    print('Task 2 started')
    time.sleep(2)
    print('Task 2 completed')


def main():
    start = time.time()
    task_1()
    task_2()
    end = time.time()
    time_elapsed = end - start
    print('Time elapsed: ' + str(time_elapsed))

if __name__ == '__main__':
    main()