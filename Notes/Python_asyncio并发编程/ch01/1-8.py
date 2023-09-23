
import time
import threading
import requests


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)



start = time.time()
thread_1.start()
thread_2.start()
print('All threads running !')
thread_1.join()
thread_2.join()
end = time.time()

print(f'Running with threads took {end - start:.4f} seconds.')

