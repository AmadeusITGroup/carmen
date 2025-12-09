"""
Cloud Metadata model of IF
"""

from pathlib import Path
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)
from backend.src.schemas.virtual_machine import VirtualMachine


class CloudMetadata(ModelUtilities):
    """
    Concrete class for the cloud-metadata model of IF to be used in retrieving physical-processor
    name and CPU TDP based on cloud instance type and vendor (which is Azure by default)
    """

    def __init__(self):

        import backend.src.services.carbon_service.impact_framework.files as files_module
        files_dir = Path(files_module.__file__).parent
        csv_path = files_dir / "azure_instances.csv"

        config = {
            "filepath": str(csv_path),
            "query": {"instance-class": "cloud/instance-type"},
            "output": [
                ["cpu-tdp", "cpu/thermal-design-power"],
                ["cpu-cores-available", "vcpus-total"],
                ["cpu-cores-utilized", "vcpus-allocated"],
                ["memory-available", "memory/requested"],
            ],
        }
        super().__init__("builtin", "CSVLookup", config=config)

    # IMP: VM specific values not time
    @staticmethod
    def fill_inputs(resource: VirtualMachine, time_index: int):
        """
        Fills the time point specific input values.

        Args:
            resource: VirtualMachine instance containing VM configuration
            time_index: Time index (unused for cloud metadata)

        Returns:
            dict: Input values for the cloud metadata lookup
        """
        return {"cloud/instance-type": resource.vm_size}
