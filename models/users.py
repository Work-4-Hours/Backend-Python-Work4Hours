from utils.db import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref

class Departament(db.Model):
    __tablename__ = 'departamentos'
    iddepartamento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable= False)

    def __init__(self,nombre):
        self.nombre= nombre


class City(db.Model):
    __tablename__ = 'ciudades'
    idciudad = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable= False)
    iddepartamento = db.Column(db.Integer, ForeignKey('departamentos.iddepartamento'),nullable=False)
    departamentos = relationship(Departament, backref=backref('departamentos', uselist=True))

    def __init__(self,nombre,iddepartamento):
        self.nombre=nombre
        self.iddepartamento=iddepartamento


class Statuses(db.Model):
    __tablename__ = 'estados'
    id = db.Column(db.Integer, primary_key=True)
    nombre_reporte = db.Column(db.String(50), nullable=False)

    def __init__(self,nombre_reporte):
        self.nombre_reporte=nombre_reporte


class Rol(db.Model):
    __tablename__ = 'roles'
    idrol = db.Column(db.Integer, primary_key=True)
    nombrerol = db.Column(db.String(15), nullable=False)

    def __init__(self,nombrerol):
        self.nombrerol=nombrerol


class Users(db.Model):
    __tablename__ = 'usuarios'
    idusuario = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(60), nullable= False)
    apellidos = db.Column(db.String(60), nullable= False)
    celular = db.Column(db.String(30), nullable= False)
    direccion = db.Column(db.String(500), nullable= False)
    correo = db.Column(db.String(500), nullable = False)
    contrasenna = db.Column(db.String(45), nullable= False)
    fnac = db.Column(db.Date, nullable= False)
    fotop = db.Column(db.String(500), nullable= True)
    ciudad = db.Column(db.Integer, ForeignKey('ciudades.idciudad'),nullable = False)
    ciudades = relationship(City, backref=backref('usuarios', uselist=True))
    rol = db.Column(db.Integer, ForeignKey('roles.idrol'),nullable= False)
    roles = relationship(Rol, backref=backref('usuarios', uselist=True))
    estado = db.Column(db.Integer, ForeignKey('estados.id'),nullable = False)
    estados = relationship(Statuses, backref=backref('usuarios', uselist=True))

    def __init__(self,nombres,apellidos,celular,direccion,correo,contrasenna,fnac,fotop,ciudad,rol,estado):
        self.nombres= nombres
        self.apellidos = apellidos
        self.celular = celular
        self.direccion = direccion
        self.correo = correo
        self.contrasenna = contrasenna
        self.fnac = fnac
        self.fotop = fotop
        self.ciudad = ciudad
        self.rol = rol
        self.estado = estado


class Categories(db.Model):
    __tablename__='categorias'
    idcategoria = db.Column(db.String, primary_key=True)
    nombrecateg = db.Column(db.String(30), nullable=True)

    def __init__(self,nombrecateg):
        self.nombrecateg=nombrecateg


class Hall(db.Model):
    __tablename__ = 'sala'
    idsala = db.Column(db.Integer, primary_key=True)
    fechainicio = db.Column(db.Date, nullable= False)
    fechafin = db.Column(db.Date, nullable= False)
    horainicio = db.Column(db.String(5), nullable= False)
    horafin = db.Column(db.String(5), nullable=False)


    def __init__(self,fechainicio,fechafin,horainicio,horafin):
        self.fechainicio=fechainicio
        self.fechafin=fechafin
        self.horainicio=horainicio
        self.horafin=horafin


class Messages(db.Model):
    __tablename__ = 'mensajes'
    idmensaje = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(1000), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    idsala = db.Column(db.Integer, ForeignKey('sala.idsala'),nullable= False)
    sala = relationship(Hall, backref=backref('mensajes', uselist=True))
    idusuario = db.Column(db.Integer, ForeignKey('usuarios.idusuario'), nullable=False)
    usuarios = relationship(Users, backref=backref('mensajes', uselist=True))

    def __init__(self, mensaje, fecha, idsala, idusuario):
        self.mensaje = mensaje
        self.fecha = fecha
        self.idsala = idsala
        self.idusuario = idusuario


class Report(db.Model):
    __tablename__ = 'reportes'
    idreporte = db.Column(db.Integer, primary_key=True)
    nombrereporte = db.Column(db.String(14), nullable=False)

    def __init__(self,nombrereporte):
        self.nombrereporte=nombrereporte


class Services(db.Model):
    __tablename__ = 'servicios'
    idservicio = db.Column(db.Integer, primary_key=True)
    idcategoria = db.Column(db.String(3), ForeignKey('categorias.idcategoria'),nullable=False)
    categorias = relationship(Categories, backref=backref('servicios', uselist=True))
    nombre = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.Integer, ForeignKey('estados.id'),nullable=False)
    estados = relationship(Statuses, backref=backref('servicios', uselist=True))
    tipo = db.Column(db.String(1), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(2000), nullable=False)
    foto = db.Column(db.String(500), nullable=False)
    usuario = db.Column(db.Integer, ForeignKey('usuarios.idusuario'),nullable=False)
    usuarios = relationship(Users, backref=backref('servicios', uselist=True))


    def __init__(self, idcategoria, nombre, estado, tipo, precio, descripción, foto, usuario):
        self.idcategoria=idcategoria
        self.nombre=nombre
        self.estado=estado
        self.tipo=tipo
        self.precio=precio
        self.descripcion=descripción
        self.foto=foto
        self.usuario=usuario

class Services_reports(db.Model):
    __tablename__ = 'servicio_reportes'
    id = db.Column(db.Integer, primary_key=True)
    idreporte = db.Column(db.Integer,ForeignKey('reportes.idreporte'), nullable=False)
    reportes = relationship(Report, backref=backref('servicio_reportes'), uselist=True)
    idservicio = db.Column(db.Integer, ForeignKey('servicios.idservicio'),nullable=False)
    servicios = relationship(Services, backref=backref('servicio_reportes'), uselist=True)


    def __init__(self, idreporte, idservicio):
        self.idreporte= idreporte
        self.idservicio= idservicio


class Users_hall(db.Model):
    __tablename__ = 'sala_usuario'
    idsalausuario = db.Column(db.Integer, primary_key=True)
    idsala = db.Column(db.Integer, ForeignKey('sala.idsala'),nullable=False)
    sala = relationship(Hall, backref=backref('sala_usuario', uselist=True))
    idusuario = db.Column(db.Integer, ForeignKey('usuarios.idusuario'),nullable=False)
    usuarios = relationship(Users, backref=backref('sala_usuario', uselist=True))

    def __init__(self, idsala, idusuario):
        self.idsala=idsala
        self.idusuario=idusuario



class User_services(db.Model):
    __tablename__ = 'usuario_reportes'
    id = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, ForeignKey('usuarios.idusuario'),nullable=False)
    usuarios = relationship(Users, backref=backref('usuario_reportes', uselist=True))
    idreporte = db.Column(db.Integer, ForeignKey('reportes.idreporte'),nullable=False)
    reportes = relationship(Report, backref=backref('usuario_reportes',uselist=True))


    def __init__(self,idusuario,idreporte):
        self.idusuario=idusuario
        self.idreporte=idreporte