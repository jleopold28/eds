from eds.plugin import Plugin


class PluginChild(Plugin):
    pass


class PluginParent(Plugin):

    @property
    def children(self):
        return [PluginChild({})]


class PluginGrandParent(Plugin):

    @property
    def children(self):
        return [PluginParent({})]


def test_get_child_plugins():
    p = PluginGrandParent({})
    assert len(p.descendants) == 2
    assert type(p.descendants[0]).__name__ == 'PluginChild'
    assert type(p.descendants[1]).__name__ == 'PluginParent'


def test_id_property():
    p = Plugin({'id': 'my_id'})
    assert p.id == 'my_id'


def test_yaml_property():
    p = Plugin({'some': 'yaml'})
    assert p.yaml == {'some': 'yaml'}
