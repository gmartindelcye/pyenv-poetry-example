from pylenium.driver import Pylenium

def test_sum():
    assert 1 + 1 == 2
    
    
def test_google(py: Pylenium):
    py.visit('http://google.com')
    py.get('[name="q"]').type('puppies')
    py.get('name="btnK"]').submit()
    assert py.should().contain_title('puppies')
    
    
    