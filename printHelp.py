import dearpygui.dearpygui as module
import inspect


l_class=[]; l_func=[]; l_otros=[]
for element in inspect.getmembers(module): 
    if inspect.isfunction(element):l_func.append(element)
    elif inspect.isclass(element):l_otros.append(element)


print(l_func)
input("..")


from os import system


