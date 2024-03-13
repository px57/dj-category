

from kernel.interfaces.interfaces import InterfaceManager
from category.__rules__.stack import CATEGORY_RULESTACK
from colorama import Fore, Style

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

    # """
    # Set selected category is database save.
    # """
    # def event_set_selected_categories(self, dbCategories):
    #     print (Fore.RED + 'DefaultRuleClass: event_set_selected_categories is empty' + Style.RESET_ALL)
    #     return True

    def relatedModelId__for__set_selected_category(self):
        """
        Return the related model id for the set selected category
        """
        return self.request.POST.get('relatedModelId')
    

    def dbCategoryRelatedTo__pre_save(self, sender, instance, **kwargs):
        """
        Receive the pre save signal
        """
        pass

    def dbCategoryRelatedTo__pre_delete(self, sender, instance, **kwargs):
        """
        Receive the pre delete signal
        """
        pass

    def dbCategoryRelatedTo__post_save(self, sender, instance, **kwargs):
        """
        Receive the post save signal
        """
        pass

CATEGORY_RULESTACK.set_rule(DefaultRuleClass)

