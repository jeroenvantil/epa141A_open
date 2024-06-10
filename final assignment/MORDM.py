def MORDM_function(dike_model, reference_scenario):
    from ema_workbench import MultiprocessingEvaluator
    with MultiprocessingEvaluator(dike_model) as evaluator:
        results = evaluator.optimize(nfe=250, reference=reference_scenario, epsilons=[0.1]*len(dike_model.outcomes))
