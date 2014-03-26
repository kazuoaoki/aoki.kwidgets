#from types import StringType

from Acquisition import aq_base, aq_inner
from AccessControl import ClassSecurityInfo

from Products.Archetypes.utils import shasattr
from Products.Archetypes.Registry import registerWidget,registerPropertyType
from Products.Archetypes.Widget import IntegerWidget


class SliderWidget(IntegerWidget):
   
    _properties = IntegerWidget._properties.copy()
    _properties.update({
        'macro': 'kwidgets-slider',
        'modes': ('view','edit'),
        'format': 'flex',
        'minimo':0,
        'maximo': 10,
        'step': 1,
        'marcadores':(),
        'helper_js': (),
        'helper_css': (),
        })
    security = ClassSecurityInfo()        


class SpinnerWidget(IntegerWidget):

    #formato: n para decimal, c para formato moeda
    #page: incremento quando usado as teclas PgUp e PgDwn    
    _properties = IntegerWidget._properties.copy()
    _properties.update({
        'macro': 'kwidgets-spinner',
        'modes': ('view','edit'),
        'format': 'flex',
        'minimo':0,
        'maximo': 10,
        'step': 1,
        'formato': 'n',
        'disabled': False,
        'page': 5,
        'helper_js': (),
        'helper_css': (),
        })
    security = ClassSecurityInfo()
    

registerWidget(SliderWidget,
               title='Slider Widget',
               description=('Uma widget para escolher valores dentro de um dado intervalo '
                            'na qual pode-se escolher deslizando um controle.'),
               used_for=('Products.Archetypes.Field.IntegerField',
                         'Products.Archetypes.Field.StringField',
                         'Products.Archetypes.Field.TextField'
                )
               )

registerWidget(SpinnerWidget,
               title='Spinner Widget',
               description=('Uma widget para escolher valores dentro de um dado intervalo '
                            'na qual pode-se escolher deslizando um controle.'),
               used_for=('Products.Archetypes.Field.IntegerField',
                         'Products.Archetypes.Field.StringField',
                         'Products.Archetypes.Field.TextField'
                )
               )

registerPropertyType('marcadores', 'tuple', SliderWidget)
#registerPropertyType('force_close_on_insert', 'boolean', SliderWidget)
