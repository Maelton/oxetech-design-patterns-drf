from django.core.management.base import BaseCommand, CommandError
from snippets.models.fornecedor import Fornecedor, Cidade
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
        
        suppliers = [];
        
        book = xlrd.open_workbook("./fornecedores.xls");
        sheet = book.sheet_by_index(0);
        
        for row in range(1, sheet.nrows):    
            name = sheet.cell_value(row, 0);
            tax_id = str(sheet.cell_value(row, 1))[:-2];
            city = sheet.cell_value(row, 2);
            street = sheet.cell_value(row, 3);
            
            if not Fornecedor.objects.filter(nome=name, cnpj=tax_id).exists():
                suppliers.append(
                    Fornecedor(
                        nome=name,
                        cnpj=tax_id,
                        cidade=Cidade.objects.filter(city).first(),
                        logradouro=street
                    )
                );
        
        Fornecedor.objects.bulk_create(suppliers);
        send_email.delay("test@gmail.com");
        
        