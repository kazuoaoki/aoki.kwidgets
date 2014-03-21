from zope.publisher.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Slider(BrowserView):
    render = ViewPageTemplateFile('templates/kslider.pt')
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
                
    def __call__(self):
        return self.index()
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request
        
    def __call__(self):
        
        return 'ok'
    """    
    #def __call__(self):
    #    pass
        
class Teste(BrowserView):
    def teste(self):
        x = self.context.REQUEST.get('amount')
        self.context.REQUEST.RESPONSE.setHeader('Content-type', 'text/html')
        self.context.REQUEST.RESPONSE.write(x)
        

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
        #import pdb;pdb.set_trace()

        value = '$("#%s").val()' %campo
        
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
        """ % { 'div': div,
                'minimo': minimo,
                'maximo': maximo,
                'value': value,
                'campo': campo,
                'step': step,
              }
        return renderjs
        

