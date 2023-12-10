from string import Template

ASSEMBLIES_PATH = "/Libs"
STUBS_PATH = "/Stubs"

class_template = Template('''
class $class_name($class_base_type):
    # isAbstract : $class_abstract
    $class_body
''')
init_template = Template('''
    def __init__(self, *args, **kwargs):
        pass                      
''')
method_template = Template(''' 
    def $method_name(self$method_args):
        return $return_val
''')

property_template = Template('''
    $property_name = property(lambda self: object(), lambda self, l:None, lambda self:None)
''')

dotnet_platform = ''' 

    ERROR:: This program runs only on NetCore 6.0 platform
    or higher.

'''

dependencies = ''' 

    ERROR:: Cannot import library:
'''

invalid_args_msg = ''' 

    ipy.bat ipyStubsGen --f"PATH_TO_DLL_FILE"
'''