from pyodbc import IntegrityError, ProgrammingError

from datos.conexion import Conexion
from dominio.estudiante import Estudiante

#new
class Print:
    pass


class EstudianteDao:
    _INSERTAR = "INSERT INTO Estudiantes ( cedula,nombre,apellido,email,carrera,activo) VALUES (?,?,?,?,?,?)"

   #new
    @classmethod
    def insertar_estudiante(cls,estudiante):
        #cursor = Conexion.obtenerCursor()
        respuesta = {'exito': False, 'mensaje': ' '}
        flag_exito = False
        mensaje = ' '
        try:
          with Conexion.obtenerCursor() as cursor:
              datos = (estudiante.cedula, estudiante.nombre, estudiante.apellido, estudiante.email, estudiante.carrera,
                       estudiante.activo)
              cursor.execute(cls._INSERTAR, datos)
        except IntegrityError as e:
            #print('La cedula que intenta ingresar ya existe')
            if e.__str__().find('Cedula') > 0:
                print('cedula ya ingresada.')
            elif e.__str__().find('Email') > 0:
                print('Email ya ingreadado')
            else:
                print('Error de integridad')


        except ProgrammingError as e:
            flag_exito = False
            print('Los datos ingresados no son del tamaño permitido')
            mensaje = 'Los datos ingresados no son del tamaño permitido'
        except Exception as e:
            flag_exito = False
            print(e)
        finally:
            respuesta['exito'] = flag_exito
            respuesta['mensaje'] = mensaje
            return respuesta





if __name__ == '__main__':
    e1 = Estudiante()
    e1.cedula = '0932548444'
    e1.nombre = 'Juan'
    e1.apellido = 'Cruz'
    e1.email = 'jcruz@mail.com'
    e1.carrera = 'ADM'
    e1.activo = True
    EstudianteDao.insertar_estudiante(e1)

