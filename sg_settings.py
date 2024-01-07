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
    """
#: isEnum : $enum_type

$enum_doc   
    """
    $enum_body
''')

class_template = Template('''
class $class_name($class_base_type):
    """
#: isAbstract : $class_abstract

$class_doc
    """
    $class_body
''')
init_template = Template('''
    def __init__(self, *args, **kwargs):
        pass                      
''')
method_template = Template(''' 
    def $method_name(self$method_args):
        """
$metd_doc
        """
        return $return_val
''')

property_template = Template('''
    $property_name = property(lambda self: object(), lambda self, l:None, lambda self:None)
    """
$property_doc
    """
''')

dotnet_platform = ''' 

    ERROR:: This program runs only on NetCore 6.0 platform
    or higher.

'''

dependencies = ''' 

    ERROR:: Cannot import library:
'''

invalid_args_msg = ''' 

    ipy.bat ipyStubsGen --f<PATH_TO_DLL_FILE>
'''

help_template = Template('''
IronPython Stubs Generator for VSCode version $version

Arguments:
--------------
--h          : this help message;
--f<dllname> : generate stubs for the 'dllname' assembly;
--l<dllname> : list the namespaces in the 'dllname' assembly;

General Usage:
--------------
- just download this project and unzip it in a folder.
- place the .NET dll for which you generate the stubs in the 'Libs' folder. 
  If a xml file (VStudio doc comments) was provided, place it here too 
  (must have the same name as the assembly).
- on Windows run: 

    C:\...\IronPython34\\net6.0\ipy.bat ipyStubsGen.ipy --f<name_of_the_dll_placed_in_Libs_folder>

- on Linux run (if ipy dotnet tool was installed):

    ipy ipyStubsGen.ipy --f<name_of_the_dll_placed_in_Libs_folder>

- the stubs files and folders are generated in the 'Stubs' folder.
- copy the generated folder into the '.ipystubs' folder inside the project's stucture.
- add to the .vscode\settings.json file in your project the following two lines:

    "python.autoComplete.extraPaths": ["$${workspaceFolder}/.ipystubs"],
    "python.analysis.extraPaths": ["$${workspaceFolder}/.ipystubs"]

''')