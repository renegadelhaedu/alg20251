valorProduto = float(input('digite o valor do produto'))
pago = float(input('digite o valor pago'))

if pago >= valorProduto:
    troco = pago - valorProduto
    if troco > 0:
        print('você comprou o produto e o troco é', troco)
    else:
        print('você comprou o produto')

else:
    falta = valorProduto - pago
    print('falta voce pagar ', falta)
    formaPagamento = input('vai pagar via pix ou cartao?')
    if formaPagamento == 'pix':
        print('a chave pix é 23984793875345')
    else:
        print('aproxime ou insira o cartao')