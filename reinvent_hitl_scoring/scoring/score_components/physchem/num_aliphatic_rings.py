from reinvent_hitl_scoring.scoring.component_parameters import ComponentParameters
from reinvent_hitl_scoring.scoring.score_components.physchem.base_physchem_component import BasePhysChemComponent


class NumAliphaticRings(BasePhysChemComponent):
    def __init__(self, parameters: ComponentParameters):
        super().__init__(parameters)

    def _calculate_phys_chem_property(self, mol):
        return self._phys_chem_descriptors.number_of_aliphatic_rings(mol)
