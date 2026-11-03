import importlib.util,json,unittest,copy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('checker',ROOT/'scripts/check_project.py');checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
class ProjectChecks(unittest.TestCase):
    def setUp(self):
        self.plan={'duration':10,'fps':30,'shots':[{'id':'one','t0':0,'t1':10}],'texts':[],'events':[{'id':'arrive','t':4},{'id':'rise','t':4.2,'requires':['arrive']}]}
    def test_valid(self):self.assertTrue(checker.check(self.plan)['passed'])
    def test_cause_order(self):
        self.plan['events'][1]['t']=3;self.assertFalse(checker.check(self.plan)['passed'])
    def test_cycle(self):
        self.plan['events'][0]['requires']=['rise'];self.assertFalse(checker.check(self.plan)['passed'])
    def test_short_title(self):
        self.plan['texts']=[{'id':'title','text':'一滴水的旅程','role':'title','t0':8.533333,'t1':10}];self.assertFalse(checker.check(self.plan)['passed'])
    def test_gap(self):
        self.plan['shots'][0]['t0']=.1;self.assertFalse(checker.check(self.plan)['passed'])
    def test_nonfinite(self):
        self.plan['duration']=float('nan');self.assertFalse(checker.check(self.plan)['passed'])
    def test_example(self):
        p=json.loads((ROOT/'examples/water-journey/project.json').read_text(encoding='utf-8'));self.assertTrue(checker.check(p)['passed'])
if __name__=='__main__':unittest.main()
