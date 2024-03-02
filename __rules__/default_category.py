

from kernel.interfaces.interfaces import InterfaceManager
from category.__rules__.stack import CATEGORY_RULESTACK

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    label = 'DEFAULT'

    allow = True


CATEGORY_RULESTACK.set_rule(DefaultRuleClass)