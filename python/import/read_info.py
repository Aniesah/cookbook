import kota.jakarta as jkt
import kota.bandung as bdg
import kota.cirebon as crb
import kota.subang as sub

print ("JKT-BDG = ", jkt.distance['Bandung'])
print ("BDG-JKT = ", bdg.distance['Jakarta'])

import kota.bandung as bdg1
print('Pusat Kecamatan Arcamanik = ', bdg1.kecamatan['Arcamanik']['pusat'])
print('Luas Kecamatan Arcamanik = ', bdg1.kecamatan['Arcamanik']['luas'])

import kabupaten.bandung as bdg2
print('Pusat Kecamatan Cimenyan = ', bdg2.kecamatan['Cimenyan']['pusat'])
print('Luas Kecamatan Cimenyan = ', bdg2.kecamatan['Cimenyan']['luas'])
