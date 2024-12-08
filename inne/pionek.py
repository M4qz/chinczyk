class Pionek:
    def __init__(self,dictionary): #, double_array,tuples_list
        #self._tuples_list = tuples_list
        self._dictionary = dictionary
        # self._double_array = double_array
    '''
    # Getter for tuples_list
    @property
    def tuples_list(self):
        return self._tuples_list

    # Setter for tuples_list
    @tuples_list.setter
    def tuples_list(self, value):
        if isinstance(value, list):
            self._tuples_list = value
        else:
            raise ValueError("tuples_list must be a list")
    '''
    # Getter for dictionary
    @property
    def dictionary(self):
        return self._dictionary

    # Setter for dictionary
    @dictionary.setter
    def dictionary(self, value):
        if isinstance(value, dict):
            self._dictionary = value
        else:
            raise ValueError("dictionary must be a dictionary")

