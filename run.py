#!/usr/local/bin/python

import dynclipy
task = dynclipy.main()

import pandas as pd
import json

import scimitar.models
import scimitar.morphing_mixture as mm

import time
checkpoints = {}

#   ____________________________________________________________________________
#   Load data                                                               ####
expression = task["expression"]
p = task["parameters"]

checkpoints["method_afterpreproc"] = time.time()

#   ____________________________________________________________________________
#   Infer trajectory                                                        ####
transition_model, pseudotimes = mm.morphing_gaussian_from_embedding(
  expression.values,
  fit_type='spline',
  degree=p["degree"],
  step_size=p["step_size"],
  cov_estimator=p["cov_estimator"],
  cov_reg=p["cov_reg"]
)

refined_transition_model, refined_pseudotimes = transition_model.refine(
  expression.values,
  max_iter=p["max_iter"],
  step_size=p["step_size"],
  cov_estimator=p["cov_estimator"],
  cov_reg=p["cov_reg"]
)

checkpoints["method_aftermethod"] = time.time()

#   ____________________________________________________________________________
#   Save output                                                             ####
pseudotime = pd.DataFrame({
  "cell_id": expression.index,
  "pseudotime": refined_pseudotimes
})

model = dynclipy.wrap_data(cell_ids = expression.index)
model.add_linear_trajectory(pseudotime = pseudotime)
model.add_timings(checkpoints)

model.write_output(task["output"])
