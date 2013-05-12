from framed.io_utils.sbml import *
from framed.core.fixes import fix_bigg_model
from framed.analysis.fba import FBA

ec_core_model = 'models/ecoli_core_model.xml'

#load SBML model, and fix BIGG model's perculiarities
model = load_sbml_model('models/ecoli_core_model.xml', kind=CONSTRAINT_BASED)
fix_bigg_model(model)

solution = FBA(model)
