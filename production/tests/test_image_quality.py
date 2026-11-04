import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from image_quality import QualityError, decision, digest, validate

class GateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.image = self.root / 'img.png'
        self.image.write_bytes(b'test-image')
        self.review = self.root / 'review.json'
        self.record = {'file':'img.png','sha256':digest(self.image),'score':95,'critical_error':False,'reviewed':True,'notes':'Review completed.'}
    def write(self): self.review.write_text(json.dumps({'images':[self.record]}))
    def test_accepted(self):
        self.write(); validate(self.review,[self.image])
    def test_critical_defect_rejected_even_100(self):
        self.record.update(score=100,critical_error=True); self.write()
        with self.assertRaises(QualityError): validate(self.review,[self.image])
    def test_unreviewed_and_low_score_rejected(self):
        self.record['score']=89; self.write()
        with self.assertRaises(QualityError): validate(self.review,[self.image])
        self.record.update(score=95,reviewed=False); self.write()
        with self.assertRaises(QualityError): validate(self.review,[self.image])
    def test_changed_image_and_missing_manifest_rejected(self):
        self.write(); self.image.write_bytes(b'changed')
        with self.assertRaises(QualityError): validate(self.review,[self.image])
        with self.assertRaises(QualityError): validate(self.root/'absent.json',[self.image])
    def test_retry_is_suggestion_not_model_execution(self):
        self.assertEqual(decision(100,True,0),'regenerate')
        self.assertEqual(decision(60,False,3),'simplify_composition')
        self.assertEqual(decision(90,False,0),'accept')

if __name__ == '__main__': unittest.main()
