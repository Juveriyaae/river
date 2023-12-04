from __future__ import annotations
from river import stats 
import pytest
from river.stats.chisquare import ChiSquare

@pytest.fixture
def chi_square_instance():
    return ChiSquare()

def test_chi_square_initialization(chi_square_instance):
    assert chi_square_instance.total_samples == 0
    assert chi_square_instance.observed_frequencies == {}

def test_chi_square_update(chi_square_instance):
  # Entering my own random data
    chi_square_instance.update('Math', 'Grade_A')
    chi_square_instance.update('Biology', 'Grade_B')
    assert chi_square_instance.total_samples == 2
    assert chi_square_instance.observed_frequencies == {'Math': {'Grade_A': 1}, 'Biology': {'Grade_B': 1}}
'''
#There is an issue with output. Displays same output always. 
Area under construction. 
Need to change the code. 
'''
def test_chi_square_transform_one(chi_square_instance):
    chi_square_instance.update('Math', 'Grade_D') #some random data
    chi_square_instance.update('Biology', 'Grade_B')
    p_value = chi_square_instance.transform_one('Math')  
    assert isinstance(p_value, float)    
  
def test_chi_square_reset(chi_square_instance):
    chi_square_instance.update('Math', 'Grade_A')
    chi_square_instance.update('Biology', 'Grade_B')
    chi_square_instance.reset()
    assert chi_square_instance.total_samples == 0
    assert chi_square_instance.observed_frequencies == {}
