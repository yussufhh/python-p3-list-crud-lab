def create_an_empty_list():
     return []

def create_a_list():
    return [2, 5, 7,8]

def add_element_to_end_of_list(my_list, new_element):
    my_list.append(new_element)
    return my_list


def add_element_to_start_of_list(l, element):
   l.insert(0, element)
   return l


def remove_element_from_end_of_list(l):
    if l:
        l.pop()
    return l

def remove_element_from_start_of_list(l):
    if l:
        del l[0]
    return l

def retrieve_first_element_from_list(l):
    if l:
        return l[0]
   

def retrieve_element_from_index(l, index):
 if 0<=index<len(l):
     return l[index]


def retrieve_last_element_from_list(l):
    if l:
     return l[-1]
