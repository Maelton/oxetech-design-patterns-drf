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

        valor = attrs['valor']
        valor_efetivado = attrs['valor_efetivado']
        vencimento = attrs['vencimento'];
        data_efetivacao = attrs['data_efetivacao'];

        if not validate_effective_date(vencimento, data_efetivacao):            
            raise serializers.ValidationError("Invalid transaction dates");

        if not validate_transaction_amounts(valor, valor_efetivado):
            raise serializers.ValidationError("Invalid transaction amounts");
        
        return attrs;
    
    def create(self, validated_data):        
        def duplicate_transaction(previous_transaction):
            """
            Quando o valor_efetivado for menor que o valor deve-se
            criar um novo registro copiando as mesmas informações,
            exceto data_efetivado e valor_efetivado.

            O valor deve ser o restante do que foi pago a menos.

            Repetição do lançamento, com 30 dias de diferença entre cada repetição.
            """
            
            from datetime import timedelta
            
            outstanding_amount = previous_transaction.valor - previous_transaction.valor_efetivado;
            
            new_transaction = Lancamento.objects.create(
                descricao=previous_transaction.descricao,
                forma_pagamento=previous_transaction.forma_pagamento,
                tipo=previous_transaction.tipo,
                categoria=previous_transaction.categoria,
                valor=outstanding_amount,
                valor_efetivado=None,
                vencimento=previous_transaction.vencimento + timedelta(days=30),
                data_efetivacao=None,
                fornecedor=previous_transaction.fornecedor,
            );

            return new_transaction;

        instance = super().create(validated_data);
        
        if instance.valor_efetivado and instance.valor_efetivado < instance.valor:
            duplicate_transaction(instance);

        return instance;