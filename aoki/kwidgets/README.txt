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
        ::step -> valor do 'salto' na escolha de um valo dado um intervalo
        
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
    atapi.IntegerField(
        name='escala',
        default=15,
        widget=SliderWidget(
            label=u"Escala",
            minimo=0,
            step=5,
            maximo=30,
        ),
