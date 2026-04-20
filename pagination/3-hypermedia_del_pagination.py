#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:

        assert type(index) is int
        assert index >= 0
        assert type(page_size) is int and page_size > 0

        data = self.indexed_dataset()
        assert index < len(data)

        collected = []
        current = index

        while len(collected) < page_size and current < len(data):
            if current in data:
                collected.append(data[current])
            current += 1

        next_index = current if current < len(data) else None

        return {
            "index": index,
            "data": collected,
            "page_size": len(collected),
            "next_index": next_index
        }