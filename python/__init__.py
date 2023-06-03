import importlib
import pkgutil

__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    if module_name != "__init__" and module_name != "main":
        __all__.append(module_name)
        _module = importlib.import_module("." + module_name, __package__)
        globals()[module_name] = _module
