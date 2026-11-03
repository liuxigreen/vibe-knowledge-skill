import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from engine.scene3d import Camera,Material
class Components(unittest.TestCase):
    def test_target_center(self):
        c=Camera((0,-5,2),(0,0,0),640,360);self.assertTrue(np.allclose(c.project((0,0,0))[:2],[320,180]))
    def test_batch(self):
        c=Camera((0,-5,2),(0,0,0),640,360);self.assertTrue(np.allclose(c.project_many([[1,0,0]])[0],c.project((1,0,0))))
    def test_invalid(self):
        with self.assertRaises(ValueError):Camera((0,0,0),(0,0,0),640,360)
    def test_topdown(self):
        self.assertTrue(np.isfinite(Camera((0,0,5),(0,0,0),640,360).project((0,0,0))).all())
    def test_lighting(self):
        m=Material((150,120,90));self.assertGreater(sum(m.shade([0,0,1])),sum(m.shade([0,0,-1])))
if __name__=='__main__':unittest.main()
