import csv
from itertools import islice
from django.conf import settings
from django.core.management.base import BaseCommand
from projects.models import Abonado

class Command(BaseCommand):
    help = 'Load data from Trafico.csv into the TRAFICO table'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'tabla_accesos.csv'
        #,ANNO,MES,COLOMBIA_TELECOMUNICACIONES,COLOMBIA_MOVIL,COMUNICACION_CELULAR_COMCEL,EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA,UNE_EPM,AVANTEL,ALMACENES_EXITO,VIRGIN_MOBILE,PARTNERS_TELECOM,SETROC_MOBILE,UFF_MOVIL,CELLVOZ_COLOMBIA,LOGISTICA_FLASH,LOV_TELECOMUNICACIONES,SUMA_MOVIL
        with open(datafile) as file:
            reader = csv.DictReader(file)
            for row in islice(reader, 1, None):
                Abonado.objects.create(
                    anno=row['ANNO'],
                    mes=row['MES'],
                    colombia_telecomunicaciones=row['COLOMBIA_TELECOMUNICACIONES'],
                    colombia_movil=row['COLOMBIA_MOVIL'],
                    comunicacion_celular_comcel=row['COMUNICACION_CELULAR_COMCEL'],
                    empresa_de_telecomunicaciones_de_bogota=row['EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA'],
                    une_epm=row['UNE_EPM'],
                    avantel=row['AVANTEL'],
                    almacenes_exito=row['ALMACENES_EXITO'],
                    virgin_mobile=row['VIRGIN_MOBILE'],
                    partners_telecom=row['PARTNERS_TELECOM'],
                    setroc_mobile=row['SETROC_MOBILE'],
                    uff_movil=row['UFF_MOVIL'],
                    cellvoz_colombia=row['CELLVOZ_COLOMBIA'],
                    logistica_flash=row['LOGISTICA_FLASH'],
                    lov_telecomunicaciones=row['LOV_TELECOMUNICACIONES'],
                    suma_movil=row['SUMA_MOVIL']
                )