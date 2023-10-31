# dentro de dearpygui instalado en sistema
# existe un demo el cual muestra las principales caracteristicas de este paquete

import dearpygui.dearpygui as dpg  #importar dearpygui
import dearpygui.demo as demo      #importar demo como objeto

dpg.create_context()                                      #creando contexto
dpg.create_viewport(title='Demo', width=600, height=600)  #creando wieqport

#------------------------

demo.show_demo()  # esta funcion desempaqueta el demo en el viewport actual

#-------------------------

dpg.setup_dearpygui() #configuraciones iniciales, se prepara dearpygui **kwargs
dpg.show_viewport()   #muestr el viewport principal, se puede configurar **kwargs
dpg.start_dearpygui() #prepara viewport, limpia los datos y lanza el mainloop       
dpg.destroy_context() #elimina contexto limpia memoria 

