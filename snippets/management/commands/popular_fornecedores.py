from django.core.management.base import BaseCommand, CommandError
from snippets.models.fornecedor import Fornecedor
from snippets.tasks import send_email
import xlrd



class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        print('Arguamentos')
        #parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        # cnpj = '29192585000171'
        # objeto, _ = Fornecedor.objects.get_or_create(
        #     cnpj=cnpj,
        #     defaults={'nome': 'Washinton Costa'}
        # )
        
        # print(objeto, _)
        
        book = xlrd.open_workbook("./fornecedores.xls")
        
        send_email.delay("test@gmail.com")
        
        