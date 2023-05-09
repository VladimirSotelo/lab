from datetime import datetime
from tinydb import TinyDB,Query
class tarea:
    def __init__(self,id,titulo,descripcion,estado,creada,actualizada):
        self.id=id
        self.titulo= titulo
        self.descripcion=descripcion
        self.estado=estado
        self.creada=creada
        self.actualizada=actualizada
class admintarea:
    def __init__(self,db_tarea):
        self.db=TinyDB('tareas')
        self.tarea=self.db.table('tarea')
    def agregar_terea(self,tarea):
        tarea_dict=tarea.__dict__
        tarea_dict['Creada']=datetime.now().strftime("%Y-%d-%m %H:%M:S")
        tarea_dict['actualizada']=tarea_dict['Creada']
        self.tarea.insert(tarea_dict)
        for i in range(self.db):
            return id(tarea)
    def traer_tarea(self,tarea_id):
        
        pass
    def actualizar_estado_tarea(self,tarea_id,estado):
        pass 
    def eliminar_tarea(self,tarea_id):
        pass 
    def traer_todas_taeras():
        pass 
