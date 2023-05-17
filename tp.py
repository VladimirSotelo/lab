from tinydb import TinyDB, Query
from datetime import datetime
from typing import List
import uuid
class Tarea:
    def __init__(self,id,titulo,descripcion,estado,creada,actualizada):
        self.id=none
        self.titulo=titulo
        self.descripcion=descripcion
        self.estado="pendiente"
        self.creada=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.actualizada=self.creada
    def __str__(self):
        return f"[{self.id}]{self.titulo}({self.estado})"

class admintarea:
    def __init__(self,db_path):
        self.db=TinyDB(db_path)
        self.tarea=Query()
    def agregar_tarea(self,tarea:Tarea)->int:
        tarea.id=len(self.tareas )+1
        self.tareas.append(tarea)
    
        tarea_dict = tarea.__dict__
        self.db.insert(tarea_dict)
        return tarea.id
    def traer_tarea(self,tarea_id:int)->Tarea:
        tarea = self.db.get(self.Tarea.id == tarea_id)
        return Tarea(**tarea)if tarea else none
    def actu_estado_tarea(self,tarea_id:int,estado:str):
        tarea = self.db.get(self.Tarea.id == tarea_id)
        if tarea:
            tarea["Estado"]=estado
            tarea["Actualizada"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.update(tarea, self.Tarea.id == tarea_id)
    def eliminar_tarea(self,tarea_id:int):
        self.db.remove(self.Tarea.id == tarea_id)
    def traer_tareas(self)->list[Tarea]:
        tareas=[]
        for tarea in self.db.all():
            tarea_id = tarea['id']
            tarea_obj=Tarea(tarea_id,tarea["titulo"],tarea["descripcion"])
            tarea_obj.estado= tarea["estado"]
            tarea_obj.creada = tarea["creada"]
            tarea_obj.actualizada= tarea["actualizada"]
            tareas.append(tarea_obj)
        return tareas

def main():
    admi_tarea=admintarea('tarea.json')
    while True:
        print("1) agragar:")
        print("2) ver:")
        print("3) actualizar:")
        print("4) eliminar:")
        print("5) ver todas las tareas")
        print("6) salir:")
        opt=input("seleccione una opcion:")

        if opt =="1":
            titulo =input("ingrese titulo: ")
            descripcion=input("ingrese una descripcion: ")
            tarea = Tarea(id,titulo,descripcion,estado,creada,actualizada)
            id=tarea_id
            print(f"tarea agregada con ID {tarea_id} ")
        elif opt == "2":
            tarea_id =input("ingrese el ID de la tarea")
            tarea=admi_tarea.traer_tarea(int(tarea_id)) 
            if tarea:
                print(tarea)
            else:
                print("no se encontro la tarea")
        elif opt == "3":
            tarea_id= input("ingrese el ID de la trea")
            estado=input("ingrese el estado de la tarea")
            admi_tarea.actu_estado_tarea(int(tarea_id, estado))            
        elif opt == "4":
            tarea_id=input("ingrese el ID de la trea")
            admi_tarea.eliminar_tarea(int(tarea_id))
            print("tarea eliminada")
        elif opt == "5":
            tarea = admi_tarea.traer_tareas()
            print("Todas las tarea:\n")
            tareas=admi_tarea.traer_tareas()
            for tarea in tareas:
                print(tarea)
        elif opt == "6":
            break
        else:
            print("opcion invalida,seleccione otra")

if __name__=="__main__":
    main()