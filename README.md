# IronPython Stubs Generator for VSCode

Arguments:
--------------
-h          : a help message;

-h1          : a more detailed help message;

-f &lt;dllname&gt; : generate stubs for the 'dllname' assembly;

-l &lt;dllname&gt; : list the namespaces in the 'dllname' assembly;

General Usage:
--------------
- just download this project and unzip it in a folder.
- place the .NET dll for which you generate the stubs in the 'Libs' folder. 
  If a xml file (VStudio doc comments) was provided, place it here too 
  (must have the same name as the assembly).
- on Windows run:

```
C:\...\IronPython34\net6.0\ipy.bat ipyStubsGen.ipy -f <name_of_the_dll_placed_in_Libs_folder>
```

- on Linux run (if ipy dotnet tool was installed):

```
ipy ipyStubsGen.ipy -f <name_of_the_dll_placed_in_Libs_folder>
```

- the stubs files and folders are generated in the 'Stubs' folder.
- copy the generated folder into the '.ipystubs' folder inside the project's stucture.
- add to the .vscode\settings.json file in your project the following two lines:

```json
"python.autoComplete.extraPaths": ["${workspaceFolder}/.ipystubs"],
"python.analysis.extraPaths": ["${workspaceFolder}/.ipystubs"]
```

# Reference

- Other similar tools:

  -- https://github.com/gtalarico/ironpython-stubs/


# Tips

- If run from VSCode (1.85.2) and the progress twirl doesn't work, then set SHOW_PROGRESS (sg_settings.py) to False. (twirl solution copied from stackoverflow.com unknown page, pending credit).