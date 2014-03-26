Introduction
============

Produto de widgets personalizados.

Requisitos:
* collective.js.jqueryui

Exemplos de uso:

*SliderWidget - Um slider que permite a seleção de um determinado 
valor dado um intervalo fornecido:
    -Fields permitidos: IntegerField e StringField
    -Parametros:
        ::minimo -> menor valor do intervalo que pode ser escolhido
        ::maximo -> maior valor do intervalo que pode ser escolhido
        ::step -> valor do 'salto' na escolha de um valor dado um intervalo
        
    -Exemplos de uso:
    
    from aoki.kwidgets.widgets import SliderWidget
    
    #basico
    atapi.IntegerField(
        name='evolucao',
        widget=SliderWidget(
            label=u"Evolucao",
            minimo=1,
            maximo=10,
        ),
    ),
    
    #nesse caso, o slider pula de 5 em 5.
    #e coloca as escalas como legenda no slider
    atapi.IntegerField(
        name='escala',
        default=15,
        widget=SliderWidget(
            label=u"Escala",
            minimo=0,
            step=5,
            maximo=30,
            marcadores=("nada", "médio", "pouco", "muito"),
        ),
        
        
        
*SpinnerWidget - widget spinner para seleção de números em um
determinado intervalo de valor. Permite que se faça incrementos 
 usando setas e 'paginações' ou incrementos maiores usando 
 PgUp e PgDwn
    -OBSERVAÇÃO: o plugin 'Spinner' deve estar ativo, através da configlet (@@jqueryui-plugins-controlpanel).
    -Fields permitidos: IntegerField e StringField
    -Parametros:
        ::minimo -> menor valor do intervalo que pode ser escolhido
        ::maximo -> maior valor do intervalo que pode ser escolhido
        ::step -> valor do 'salto' na escolha de um valor dado um intervalo, quando 
                  as setas são utilizadas. Padrão: 1
        ::formato -> Se decimal ('d') ou moeda ('c'). Padrão: 'd'
        ::disabled -> desabilita o widget para edição
        ::page -> 'paginação'; valor do salto quando as teclas PgUp ou PdDwn são 
                  utilizadas. Padrão: 5

    -Exemplos de uso:
    
    from aoki.kwidgets.widgets import SpinnerWidget
    
    #basico
    atapi.IntegerField(
        name='valores-teste',
        widget=SpinnerWidget(
            label=u"Selecione um valor",
            minimo=1,
            maximo=10,
        ),
    ),
    
    #salto de 10 em 10 quando teclamos PgUp ou PgDown
    atapi.IntegerField(
        name='idade',
        widget=SliderWidget(
            label=u"Idade",
            minimo=0,
            page=10,
            maximo=130,
        ),

