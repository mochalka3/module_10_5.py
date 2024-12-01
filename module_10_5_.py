import time
from multiprocessing import Pool

def read_info(filename):
    all_data = []
    with open(filename, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            all_data.append(line)
    return all_data

if __name__ == '__main__':
    filenames = [f'./file_{i}.txt' for i in range(1, 5)]  # Список имен файлов

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        data = read_info(filename)
    end_time = time.time()
    linear_execution_time = end_time - start_time
    print(f'Линейное выполнение заняло: {linear_execution_time:.6f} секунд')

    # Многопроцессорный вызов
    start_time = time.time()
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    end_time = time.time()
    multiprocessing_execution_time = end_time - start_time
    print(f'Многопроцессорное выполнение заняло: {multiprocessing_execution_time:.6f} секунд')
