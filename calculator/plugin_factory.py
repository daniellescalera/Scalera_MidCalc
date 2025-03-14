import importlib
import os

class PluginFactory:
    """Factory class to dynamically load plugins."""

    @staticmethod
    def load_plugins(plugin_dir="plugins"):
        """Dynamically loads all plugins from the specified folder."""
        plugins = {}

        if os.path.exists(plugin_dir):
            for filename in os.listdir(plugin_dir):
                if filename.endswith(".py") and filename != "__init__.py":
                    module_name = f"{plugin_dir.replace('/', '.')}.{filename[:-3]}"  # Convert path to module
                    module = importlib.import_module(module_name)
                    if hasattr(module, "plugin_info"):
                        info = module.plugin_info()
                        plugins[info["command"]] = info
        return plugins
