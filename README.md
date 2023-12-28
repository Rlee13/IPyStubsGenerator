# IronPython Stubs Generator for VSCode

Usage:
- just download this project and unzip it in a folder.
- place the .NET dll in the Libs folder. If a xml file for docs was provided place it here too (must have the same name as the assembly).
- run 
```
C:\...\IronPython34\net6.0\ipy.bat -X:FullFrames ipyStubsGen.ipy --fname_of_the_dll_placed_in_Libs_folder
```

- the stubs files and folders are generated in the Stubs folder.
- Copy the generated folder into the .ipystubs folder inside the project's stucture.
- add to the .vscode\settings.json file in your project these two lines:
```json
"python.autoComplete.extraPaths": ["${workspaceFolder}/.ipystubs"],
"python.analysis.extraPaths": ["${workspaceFolder}/.ipystubs"]
```

# Reference

- Other similar tools:

  -- https://github.com/gtalarico/ironpython-stubs/