from typing import Any
from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.checks.resource.base_spec_check import BaseK8Check


class DatabaseSize(BaseK8Check):
    def __init__(self) -> None:
        name = "Ensure databaseSizeGb is between 1 and 100 in MyCustomDatabase"
        id = "CKV_K8S_CUSTOM_DB_3"
        supported_kind = (
            "MyCustomDatabase",
        )
        categories = (CheckCategories.KUBERNETES,)
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_kind)

    def scan_spec_conf(self, conf: dict[str, Any]) -> CheckResult:
        spec = conf.get('spec')
        if spec:
            if "databaseSizeGb" in spec:
                if type(spec['databaseSizeGb']) is not int:
                    return CheckResult.FAILED
                if spec['databaseSizeGb'] > 100 or spec['databaseSizeGb'] < 1:
                    return CheckResult.FAILED
                return CheckResult.PASSED
            return CheckResult.FAILED
        return CheckResult.FAILED


check = DatabaseSize()
