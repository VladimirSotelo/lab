from tinydb import TinyDB ,Query
from datetime import datetime
import taks

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
    def agregar_tarea(self,tarea):
        tarea_dict=tarea.__dict__
        tarea_dict['creada']=datetime.now().strftime("%Y-%m-%d H%:%M:%S")
        tarea_dict['actualizada']=tarea_dict['creada']
        self.Tarea.inser(tarea_dict)
    def traer_tarea(self,tarea_id):
        tarea = Query()
        resul=self.tarea.search(tarea.id == tarea_id)
        if resultado:
            tarea_dict = resul[0]
            tarea_dict['creada']=datetime.strptime(tarea_dict['creada'],"%Y-%m-%d H%:%M:%S")
            tarea_dict['actualizada']=datetime.strptime(tarea_dict['actualizada'], "%Y-%m-%d H%:%M:%S")
            return tarea(**tarea_dict)
        else:
            return None
    def actu_estado_tarea(self,tarea_id,estado):
        tarea=Query()
        self.tarea.update({'estado':estado,'actualizada':datetime.strftime(tarea_id['actulaizada'],"%Y-%m-%d H%:%M:%S")},Tarea.id==tarea_id)
    def eliminar_tarea(self,tarea_id):
        tarea=Query()
        self.tarea.remove(tarea.id==tarea_id)
    def traer_todo(self):
        resultado=self.Tarea.all()
        for tarea_dict in resultado:
            tarea_dict['creada'] =datetime.strptime(tarea_dict['creada'],"%Y-%m-%d H%:%M:%S") 
            tarea_dict['actualizada']=datetime.strptime(tarea_dict['actualizada'], "%Y-%m-%d H%:%M:%S")

def main():
    mi_tarea=tarea(id, titulo, descripcion, estado, creada, actualizada)
    ADMIN=admintarea('tareas') 
    
    print("1) agragar:")
    print("2) editar:")
    print("3) buscar:")
    print("4) buscar todo:\n")
    
    
    
    