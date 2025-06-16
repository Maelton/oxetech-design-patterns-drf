from django.core.management.base import BaseCommand, CommandError
from snippets.models.fornecedor import Fornecedor
import xlrd



class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        print('Arguamentos')
        #parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        cnpj = '29192585000171'
        objeto, _ = Fornecedor.objects.get_or_create(
            cnpj=cnpj,
            defaults={'nome': 'Washinton Costa'}
        )
        
        print(objeto, _)
        
        book = xlrd.open_workbook("myfile.xls")
        print("The number of worksheets is {0}".format(book.nsheets))
        print("Worksheet name(s): {0}".format(book.sheet_names()))
        sh = book.sheet_by_index(0)
        print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
        print("Cell A30 is {0}".format(sh.cell_value(rowx=30, colx=0)))
        for rx in range(sh.nrows):
            print(sh.row(rx))
        
        