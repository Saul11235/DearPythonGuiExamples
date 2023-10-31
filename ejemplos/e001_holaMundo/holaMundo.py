# primer ejemplo usando dearpygui

# importando lib
import dearpygui.dearpygui as dpg

dpg.create_context()
# creando contexto, se puede añadir **kwargs
# en este caso el contexto estara vacio
# context:
# en este framework  este es un objeto que abstrae
# la representacion de cada viewport y sus interacciones
# el context contiene varios viewports

dpg.create_viewport(title='viewport', width=600, height=300)
# create_viewport **args, tienen varios argumentos para 
# configurar el viewport, los datos no ingresados son
# los datos por defecto
# en este modulo  definimos un viewport este viewport
# se encargara de contener los archivos, 

#-------------------------------------------

with dpg.window(label="ventana"):  #width se usa con ADMINISTRADOR DE CONTEXTO
    dpg.add_text("Hola mundo!")
    # colocamos  un texto en window

#-------------------------------------------

dpg.setup_dearpygui() #configuraciones iniciales, se prepara dearpygui **kwargs
dpg.show_viewport()   #muestr el viewport principal, se puede configurar **kwargs
dpg.start_dearpygui() #prepara viewport, limpia los datos y lanza el mainloop       
dpg.destroy_context() #elimina contexto limpia memoria 


