# -*- coding: utf-8 -*-
from lettuce import step , world
from app.Examen1 import Examen1

@step(u'Cuando introdusco el numero "([^"]*)"')
def cuando_introdusco_el_numero_group1(step, num1):
    world.num1 = int(num1)
    ex = Examen1()
    world.resultado = ex.box(num1)

@step(u'El resultado debe ser "([^"]*)"')
def el_resultado_debe_ser_group1(step, esperado):
    assert world.resultado == esperado, 'Los valores no coinciden'
