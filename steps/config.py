from zenml.steps import StepParameters


class ModelNameConfig(BaseParameters):
   
    model_name: str = "lightgbm"
    fine_tuning: bool = False
