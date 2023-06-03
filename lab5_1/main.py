# Porównaj zapisywanie i odczytywanie kolekcji (100, 10000, 100000 elementów)
# za pomocą trzech technik: modułu `pickle`, `parquet` i `xlsx`.

import pickle
import pandas as pd
import time


def write_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def read_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


def write_parquet(data, filename):
    with open(filename, 'wb') as f:
        df = pd.DataFrame(data, columns=['value'])
        df.to_parquet(f, engine='pyarrow', compression='zstd')


def read_parquet(filename):
    with open(filename, 'rb') as f:
        df = pd.read_parquet(f, engine='pyarrow')
    return df.to_dict()


def write_xlsx(data, filename):
    with open(filename, 'wb') as f:
        df = pd.DataFrame(data)
        df.to_excel(f)


def read_xlsx(filename):
    with open(filename, 'rb') as f:
        df = pd.read_excel(f)
    return df.to_dict()


# timing functions
def time_execution(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return end - start


if __name__ == '__main__':
    pickle_read_times = []
    pickle_write_times = []

    parquet_read_times = []
    parquet_write_times = []

    xlsx_read_times = []
    xlsx_write_times = []

    elements_100 = list(range(100))
    elements_10000 = list(range(10000))
    elements_100000 = list(range(100000))

    pickle_write_times.append(time_execution(write_pickle, elements_100, 'pickle100'))
    pickle_write_times.append(time_execution(write_pickle, elements_10000, 'pickle_10000'))
    pickle_write_times.append(time_execution(write_pickle, elements_100000, 'pickle_100000'))

    pickle_read_times.append(time_execution(read_pickle, 'pickle_100'))
    pickle_read_times.append(time_execution(read_pickle, 'pickle_10000'))
    pickle_read_times.append(time_execution(read_pickle, 'pickle_100000'))

    parquet_write_times.append(time_execution(write_parquet, elements_100, 'parquet_100'))
    parquet_write_times.append(time_execution(write_parquet, elements_10000, 'parquet_10000'))
    parquet_write_times.append(time_execution(write_parquet, elements_100000, 'parquet_100000'))

    parquet_read_times.append(time_execution(read_parquet, 'parquet_100'))
    parquet_read_times.append(time_execution(read_parquet, 'parquet_10000'))
    parquet_read_times.append(time_execution(read_parquet, 'parquet_100000'))

    xlsx_write_times.append(time_execution(write_xlsx, elements_100, 'xlsx_100'))
    xlsx_write_times.append(time_execution(write_xlsx, elements_10000, 'xlsx_10000'))
    xlsx_write_times.append(time_execution(write_xlsx, elements_100000, 'xlsx_100000'))

    xlsx_read_times.append(time_execution(read_xlsx, 'xlsx_100'))
    xlsx_read_times.append(time_execution(read_xlsx, 'xlsx_10000'))
    xlsx_read_times.append(time_execution(read_xlsx, 'xlsx_100000'))

    print('Pickle write times:    {}'.format(pickle_write_times))
    print('Pickle read times:     {}'.format(pickle_read_times))

    print('Parquet write times:   {}'.format(parquet_write_times))
    print('Parquet read times:    {}'.format(parquet_read_times))

    print('Xlsx write times:      {}'.format(xlsx_write_times))
    print('Xlsx read times:       {}'.format(xlsx_read_times))
