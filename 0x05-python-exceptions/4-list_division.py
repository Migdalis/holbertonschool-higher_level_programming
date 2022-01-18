#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError as err:
            print("{}".format(err))
            x = 0
        except TypeError:
            print("wrong type")
            x = 0
        except IndexError:
            print("out of range")
            x = 0
        finally:
            new_list.append(x)
    return (new_list)
