import threading
import os

def foo():
    pid = os.getpid()
    tid = threading.get_native_id()
    print(f"foo: PID={pid}, Thread ID={tid}")

def bar():
    pid = os.getpid()
    tid = threading.get_native_id()
    print(f"bar: PID={pid}, Thread ID={tid}")

def baz():
    pid = os.getpid()
    tid = threading.get_native_id()
    print(f"baz: PID={pid}, Thread ID={tid}")

if __name__ == "__main__":
    thread1 = threading.Thread(target=foo) # 첫 번째 스레드 생성, 실행할 함수는 foo
    thread2 = threading.Thread(target=bar) # 두 번째 스레드 생성, 실행할 함수는 bar
    thread3 = threading.Thread(target=baz) # 세 번째 스레드 생성, 실행할 함수는 baz

    thread1.start()
    thread2.start()
    thread3.start()


"""
실행 결과
foo: PID=64009, Thread ID=2451153
bar: PID=64009, Thread ID=2451154
baz: PID=64009, Thread ID=2451155
"""