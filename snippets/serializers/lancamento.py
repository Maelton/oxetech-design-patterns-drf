from rest_framework import serializers
from snippets.models.lancamento import (Lancamento)

class LancamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lancamento
        fields = '__all__'

    def validate(self, attrs):
        def validate_effective_date(due_date, effective_date):
            """Validar data de efetivação"""
            
            return effective_date <= due_date;

        def validate_transaction_amounts(amount, effective_amount):
            """Validar valores"""
            
            return amount >= 0 and effective_amount >= 0;

        def duplicate_transaction(previous_transaction):
            """
            Quando o valor_efetivado for menor que o valor deve-se
            criar um novo registro copiando as mesmas informações,
            exceto data_efetivado e valor_efetivado.

            O valor deve ser o restante do que foi pago a menos.

            Repetição do lançamento, com 30 dias de diferença entre cada repetição.
            """
            
            pass

        valor = attrs['valor']
        valor_efetivado = attrs['valor_efetivado']
        vencimento = attrs['vencimento'];
        data_efetivacao = attrs['data_efetivacao'];

        if not validate_effective_date(vencimento, data_efetivacao):            
            raise serializers.ValidationError("Invalid transaction dates");

        if not validate_transaction_amounts(valor, valor_efetivado):
            raise serializers.ValidationError("Invalid transaction amounts");

        if valor_efetivado and valor_efetivado < valor:
            duplicate_transaction();
        
        return attrs