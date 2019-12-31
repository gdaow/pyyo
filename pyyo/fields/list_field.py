"""List field class & utilities."""
from gettext import gettext as _

from yaml import SequenceNode

from pyyo.errors import parse_error
from .base_field import BaseField


class ListField(BaseField):
    """String YAML object field."""

    def __init__(self, item_field: BaseField, *args, **kwargs):
        """Initialize list field.

        Arg:
            item_field (pyyo.BaseField) : Field used to deserialize list items.
            *args, **kwargs (list, dict) : Arguments forwarded to BaseField.

        """
        super().__init__(*args, **kwargs)
        self._item_field = item_field

    def deserialize(self, node):
        """See pyyo.BaseField.deserialize for usage."""
        if not isinstance(node, SequenceNode):
            parse_error(node, _('Expected a sequence'))

        return [self._item_field.deserialize(it) for it in node.value]
