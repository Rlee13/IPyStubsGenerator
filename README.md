# IronPython Stubs Generator for VSCode

Usage:
- place the .NET dll in the Libs folder.
- C:\...\IronPython34\net6.0\ipy.bat -X:FullFrames ipyStubsGen.ipy --fname_of_the_dll_placed_in_Libs_folder
- the stubs are generated in the Stubs folder.
- Copy the generated folder into the .stubs folder inside the project's stucture.
- add the .stub folder to the "python.analysis.extraPaths" setting in settings.json in your project.
