from tinydb import TinyDB, Query
from datetime import datetime
from typing import List

db=TinyDB('tarea.json')
Tarea = Query()
class Tarea:
    def __init__(self,titulo,descripcion):
        self.id= None
        self.titulo=titulo
        self.descripcion=descripcion
        self.estado="vivito y coliando"
        self.creada=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.actualizada=self.creada

class admin_tarea:
    @staticmethod
    def agregar_tarea(self,tarea:Tarea)->int:
        tarea.id=db.insert(tarea.__dict__)
        return tarea.id
    @staticmethod
    def traer_tarea(self,tarea_id:int)->Tarea:
        resultado=db.get(Tarea.id == tarea_id)
        if resultado:
            tarea = Tarea(**resultado)
            return resultado
        else:
            return None
    @staticmethod
    def actu_estado_tarea(self,tarea_id:int,estado:str):
        db.update({'estado':estado,'actualizada':datetime.now().strftime("%Y-%m-%d %H:%M:%S")},Tarea.id ==tarea_id)

    @staticmethod 
    def eliminar_tarea(self,tarea_id:int):   
        db.remove(Tarea.id==tarea_id)
    @staticmethod
    def traer_tareas(self)->list[Tarea]:
        tareas=[]
        resultados=db.all()
        for resultado in resultados:
            tarea =Tarea(**resultado)
            tarea.append(tarea)
        return tareas
    
def mostrar_tarea(self,tareas):
    print("todas las tareas")
    for tarea in tareas:
        print(f"id:{tarea.id},titulo:{tarea.titulo},estado{tarea.esatado},")

def main():
    while True:
        print("1) agragar:")
        print("2) ver:")
        print("3) actualizar:")
        print("4) eliminar:")
        print("5) ver todas las tareas")
        print("6) salir:")
        opt=input("seleccione una opcion:")
        if opt=="1":
            titulo =input("ingrese titulo: ")
            descripcion=input("ingrese una descripcion: ")
            nueva_tarea=Tarea(titulo,descripcion)
            
            tarea_id=admin_tarea.agregar_tarea(nueva_tarea)
            print(f"tarea agregada con ID: {tarea_id}")
        elif opt== "2":
            tarea_id =int(input("ingrese el ID de la tarea"))
            tarea=admin_tarea.traer_tarea()
            if tarea:
                print(f"Titulo:{tarea.titulo},Descripcion:{tarea.descripcion},Estado:{tarea.estado}")
            else:
                print("no se encontro la tarea")
        elif opt=="3":
            tarea_id = int(input("ingrese el ID de la tarea:"))
            estado=input("Ingreses el nuevo estado:")
            admin_tarea.actu_estado_tarea()
            print("el estado de la tarea fue actualizado")
        elif opt =="4":
            tarea_id=int(input("ingrese el ID de la trea"))      
            admin_tarea.eliminar_tarea(tarea_id)
            print("Tarea eliminada")
        elif opt =="5":
            tareas =admin_tarea.traer_tareas()
            mostrar_tarea(tareas)
        elif opt == "6":
            print("salir:")
            break
        else:
            print("opcion invalida:")

if __name__=="__main__":
    main()