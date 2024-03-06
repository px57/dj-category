

from kernel.interfaces.interfaces import InterfaceManager
from category.__rules__.stack import CATEGORY_RULESTACK

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    label = 'DEFAULT'

    """
    Max categories per user

    If the value is '*', then there is no maximum
    """
    max_categories_per_user = 3

    """
    Min categories per user

    If the value is '*', then there is no minimum
    """
    min_categories_per_user = 2

CATEGORY_RULESTACK.set_rule(DefaultRuleClass)