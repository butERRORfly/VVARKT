import krpc
from orbit import *

conn = krpc.connect(name='Коммивояжеры')
vessel = conn.space_center.active_vessel
space_center = conn.space_center

orbit(vessel, conn)