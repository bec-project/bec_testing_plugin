# Macros

This directory holds macros which are loaded automatically when starting BEC, and the default macro
config `config.yaml` which says how they are arranged in the `bec.macros` namespace.
Macros are small functions to make repetitive tasks easier. They are accessible from the BEC console,
and the client which loads a macro config shares it with all other connected clients.
Please do not put any code outside of function definitions here. If you wish for code to be automatically run when starting BEC, see the startup script at bec_testing_plugin/bec_ipython_client/startup/post_startup.py

## Layout

`config.yaml` references this directory, so its contents are merged into `bec.macros`: each python
file becomes a namespace of its functions, and each subdirectory a nested namespace. For example:

```
macros/
  macro_test.py                 -> bec.macros.macro_test.macro_test()
  alignment/
    x.py                        -> bec.macros.alignment.x.align_x()
    y.py                        -> bec.macros.alignment.y.align_y()
    fine/
      center_beam.py            -> bec.macros.alignment.fine.center_beam.center_beam()
```

Files and directories whose names start with an underscore are ignored. The same layout applies to
the user macro directory from the service config (`user_macros.base_path`), referenced in
`config.yaml` as `<user_macros>`.

Individual macros can also be referenced in `config.yaml` by module or file, see the comments there.
Macros listed under `global_in_interactive_shell` are additionally available directly in the console.

For a guide on writing macros, please see: https://bec.readthedocs.io/en/latest/user/command_line_interface.html#how-to-write-a-macro
