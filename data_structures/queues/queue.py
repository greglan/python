# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Queue(list):
    """ Simple queue implementation """
    def empty(self):
        return not self
    
    def put(self, item):
        self.append(item)

    def get(self):
        try:
            return self.pop(0)
        except IndexError:
            raise Exception("Empty queue")
