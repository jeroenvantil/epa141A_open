def MORDM_function(dike_model, reference_scenario, nfe, epsilons, convergence):
    from ema_workbench import MultiprocessingEvaluator, Scenario, ScalarOutcome

    with MultiprocessingEvaluator(dike_model) as evaluator:
        results, convergence = evaluator.optimize(nfe=nfe, reference=reference_scenario, epsilons=[epsilons]*len(dike_model.outcomes)
                                     ,convergence=convergence)
        return results, convergence

