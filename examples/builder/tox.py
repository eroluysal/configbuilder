from configbuilder.builder.tox import ToxBuilder

print ToxBuilder('tox', envlist='py26,py27')

print ToxBuilder('testenv', deps='pytest', commands='py.test')
