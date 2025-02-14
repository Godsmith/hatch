class VersionSourceInterface(object):  # no cov
    """
    Example usage:

    === ":octicons-file-code-16: plugin.py"

        ```python
        from hatchling.version.source.plugin.interface import VersionSourceInterface


        class SpecialVersionSource(VersionSourceInterface):
            PLUGIN_NAME = 'special'
            ...
        ```

    === ":octicons-file-code-16: hooks.py"

        ```python
        from hatchling.plugin import hookimpl

        from .plugin import SpecialVersionSource


        @hookimpl
        def hatch_register_version_source():
            return SpecialVersionSource
        ```
    """

    PLUGIN_NAME = ''
    """The name used for selection."""

    def __init__(self, root, config):
        self.__root = root
        self.__config = config

    @property
    def root(self):
        """
        The root of the project tree as a string.
        """
        return self.__root

    @property
    def config(self):
        """
        === ":octicons-file-code-16: pyproject.toml"

            ```toml
            [tool.hatch.version]
            ```

        === ":octicons-file-code-16: hatch.toml"

            ```toml
            [version]
            ```
        """
        return self.__config

    def get_version_data(self):
        """
        :material-align-horizontal-left: **REQUIRED** :material-align-horizontal-right:

        This should return a mapping with a `version` key representing the current version of the project and will be
        displayed when invoking the [`version`](../cli/reference.md#hatch-version) command without any arguments.

        The mapping can contain anything else and will be passed to
        [set_version](version-source.md#hatchling.version.source.plugin.interface.VersionSourceInterface.set_version)
        when updating the version.
        """
        raise NotImplementedError

    def set_version(self, version, version_data):
        """
        This should update the version to the first argument with the data provided during retrieval.
        """
        raise NotImplementedError
