from django.forms import (
    ModelForm,
    BaseInlineFormSet,
    ModelChoiceField,
    CharField,
    IntegerField,
)
from django.forms.widgets import (
    TextInput,
    HiddenInput,
)
from prngmgr.models import *
from prngmgr.settings import *

class NetworkIXLanChoiceField(ModelChoiceField):
    def label_from_instance(self, netixlan):
        label = "%s // %s // %s" % (netixlan.ixlan.ix.name, netixlan.ipaddr4, netixlan.ipaddr6)
        return label

class PeeringRouterForm(ModelForm):
    class Meta:
        model = PeeringRouter
        fields = ['hostname']

class PeeringRouterIXInterfaceForm(ModelForm):
    # netixlan = CharField(
    #     label='IXP Interface',
    #     widget=TextInput(attrs={'readonly': True})
    # )
    class Meta:
        model = PeeringRouterIXInterface
        fields = ['prngrtr', 'netixlan']
        widgets = {
            'prngrtr': HiddenInput,
        }

class NewPeeringRouterIXInterfaceForm(PeeringRouterIXInterfaceForm):
    netixlan = NetworkIXLanChoiceField(
        queryset=NetworkIXLan.objects.filter(net__asn=MY_ASN),
        label='IXP Interface'
    )