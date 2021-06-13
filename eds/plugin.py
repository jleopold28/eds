"""eds.plugin module."""

from __future__ import annotations
from typing import Dict, List


class Plugin():
    """Base class for EDS plugins."""

    eds_schema: Dict = {}
    properties_schema: Dict = {}

    def __init__(self, yaml: Dict):
        """Plugin Consructor.

        Args:
            yaml (Dict): Plugin yaml dict.
        """
        self._yaml = yaml
        self._validate()
        self.overridden = False

    def _validate(self) -> None:
        """Validate against the plugin schema.

        Also, call `validate()` for custom validation.
        """
        self.validate()

    def validate(self) -> None:
        """Abstract method implemented in plugin classes for custom validation."""
        pass

    @property
    def id(self) -> str:
        """The plugin id.

        Returns:
            str: The plugin id.
        """
        return self._yaml['id']

    @property
    def yaml(self) -> Dict:
        """The plugin yaml.

        Returns:
            Dict: The plugin yaml.
        """
        return self._yaml

    @property
    def children(self) -> List[Plugin]:
        """The list of child plugins.

        Returns:
            List[Plugin]: The list of child plugins.
        """
        return []

    @property
    def descendants(self) -> List[Plugin]:
        """The list of descendant plugins.

        Returns:
            List[Plugin]: The list of descendant plugins.
        """
        plugins = []
        for plugin in self.children:
            plugins += plugin.children
            plugins.append(plugin)
        return plugins
