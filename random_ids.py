import hashlib
import random
import numpy as np


def hash_int(int_num):
    hashed_num = hashlib.md5(str(int_num).encode())
    return hashed_num.hexdigest()


class RandomIdsGenerator:
    """
    Generate random ids from specific numbers of auto generated unique ids.
    For instance: you maybe want to generate 1000 random user ids from 10 unique ids.
    How it works: it generate random number in specific range and hash this number using md5
     and convert it to hexdigest
    """
    __slots__ = ['__n_unique_id', '__start_num', '__end_num']
    MAX_RANGE = 1000000

    def __init__(self, n_unique_id: int, start_seed: int = None):
        """
        Initialize RandomIdsGenerator
        :param n_unique_id: number of unique ids you desire
        :param start_seed: start number of the unique ids,
                Default is None that will pick up a number between (0:1000000)
                you can can use if you want generate ids in specific ranges.
        """
        self.__n_unique_id = n_unique_id
        self.__start_num = start_seed
        if not self.__start_num:
            self.__start_num = random.randrange(RandomIdsGenerator.MAX_RANGE)
        self.__end_num = self.__start_num + n_unique_id - 1

    def random(self):
        """
        Generate single random id
        :return: random id
        """
        random_num = random.randrange(self.__start_num, self.__end_num)
        return hash_int(random_num)

    def randoms(self, n_ids: int):
        """
        Generate list of random ids
        :param n_ids: number of id you need to generate
        :return: list of random ids it might contains duplications
        """
        random_numbers = np.random.randint(low=self.__start_num, high=self.__end_num, size=n_ids)
        v_hash_func = np.vectorize(hash_int)
        return v_hash_func(random_numbers)

    def get_unique_ids(self):
        """
        :return: list of unique ids it randomize from
        """
        unique_ids = []
        for i in range(self.__start_num, self.__end_num + 1):
            hashed_num = hashlib.md5(str(i).encode())
            unique_ids.append(hashed_num.hexdigest())
        return unique_ids
