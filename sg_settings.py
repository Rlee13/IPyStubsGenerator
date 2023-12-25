from string import Template

ASSEMBLIES_PATH = "/Libs"
STUBS_PATH = "/Stubs"

init_file_header_template = Template('''
# assembly_title            = $assembly_title
# assembly_version          = $assembly_version
# assembly_target_framework = $assembly_target_framework
# file_version              = $file_version
# product_version           = $product_version
# assembly_description      = $assembly_description
# assembly_product          = $assembly_product
# assembly_company          = $assembly_company
# assembly_copyright        = $assembly_copyright
# assembly_trademark        = $assembly_trademark

# Stub info generated by ipyStubsGen version $version.
''')

enum_template = Template('''
class $enum_name(Enum):
    # isEnum : $enum_type                         
    $enum_body
''')

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
        $property_doc                             
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