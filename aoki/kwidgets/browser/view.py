from zope.publisher.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class CreateSlider(BrowserView):
    """
        Gera o script necessario para renderizar o slider correspondente.
    """
    
    def __call__(self, field):

        campo = field.getName()
        div = 'kwidget-slider-' + campo
        widget = field.widget
        minimo = widget.minimo
        maximo = widget.maximo
        step = widget.step
        marcadores = widget.marcadores

        value = '$("#%s").val()' %campo
        
        saida=""
            
        if len(marcadores)>1:
            id_elemento = 'kwidget-slider-' + campo + '-scale'
            arr_itens = range(len(marcadores))
            perc = 1.0 / (len(marcadores)-1)
            saida = "<div class='ui-slider ui-slider-horizontal' id='%s' style='top:0.8em; width:100%%'>" % (id_elemento)
            if len(marcadores)==2:
                saida = saida + '<span style="position:relative;float:left; width:50%%; text-align:left">%s</span>' % (marcadores[0])
                saida = saida + '<span style="position:relative;float:left; width:50%%; text-align:right">%s</span>' % (marcadores[1])
            else:
                    for i in arr_itens:
                        #tratamento diferente para os 2 ultimos: 
                        # divide em 2 e coloca o ultimo elemento com alinhamento a direita
                        if i==(len(arr_itens)-2):
                            saida = saida + '<span style="position:relative;float:left;width:%s%%">' % (str(perc*100))
                            saida = saida + '  <span style="float:left;position:relative;width:50%%;text-align:left">%s</span>' % (marcadores[i])
                        elif i==(len(arr_itens)-1):
                            saida = saida + '  <span style="float:left;position:relative;width:50%%;text-align:right">%s</span>' % (marcadores[i])
                            saida = saida + '</span>'
                        else:
                            saida = saida + '<span style="position:relative;float:left;width:%s%%">%s</span>' % (str(perc*100), marcadores[i])
                        
            saida = saida + "</div>"
        
        renderjs = """
              <script type='text/javascript'>
              $(function() {
                $( "#%(div)s" ).slider({
                  range: "max",
                  min: %(minimo)s,
                  max: %(maximo)s,
                  value: %(value)s,
                  step: %(step)s,
                  slide: function( event, ui ) {
                    $( "#%(campo)s" ).val( ui.value );
                  }
                });
                $( "#%(campo)s" ).val( $( "#%(div)s" ).slider( "value" ) );
              });
              </script>
              %(controle)s
        """ % { 'div': div,
                'minimo': minimo,
                'maximo': maximo,
                'value': value,
                'campo': campo,
                'step': step,
                'controle': saida,
              }
        return renderjs
        

class CreateSliderScales(BrowserView):
    """
        Exibe as escalas como leganda no widget
    """
    
    def __call__(self, field):
  
        itens = field.widget.marcadores
     
        if len(itens)==0:
            return u''
            
        id_elemento = 'kwidget-slider-' + field.getName() + '-scale'
        arr_itens = range(len(itens))
        try:
            perc = 1.0 / (len(itens)-1)
            saida = "<div class='ui-slider ui-slider-horizontal' id='%s' style='top:0.8em; width:100%'>" % (id_elemento)
            for i in arr_itens:
                saida = saida + '<span style="position:relative;left:%s%">%s</span>' % (str(i*perc*100), itens[i])
            saida = saida + "</div>"

            return saida
        except:
            return ''


class CreateSpinner(BrowserView):
    """
        Spinner widget js generator.
    """
    
    def __call__(self, field):
        campo = field.getName()
        widget = field.widget
        minimo = widget.minimo
        maximo = widget.maximo
        step = widget.step
        formato = widget.formato
        disabled = str(widget.disabled).lower()
        page = widget.page
 
        #import pdb;pdb.set_trace()

        value = '$("#%s").val()' %campo
        
        renderjs = """
              <script type='text/javascript'>
             $(function() {
                $("#%(campo)s").spinner({
                  range: "max",
                  min: %(minimo)s,
                  max: %(maximo)s,
                  value: %(value)s,
                  step: %(step)s,
                  numberFormat: "%(formato)s",
                  disabled: %(disabled)s,
                  page: %(page)s
                });
             });
              </script>
        """ % { 'minimo': minimo,
                'maximo': maximo,
                'value': value,
                'campo': campo,
                'step': step,
                'formato': formato,
                'disabled': disabled,
                'page': page,
              }
        return renderjs

