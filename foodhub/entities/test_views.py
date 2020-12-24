import pytest
from django.test import Client
import time
import os 

class TestApp:
    def test_1(self):
        '''
            To test homepage
        '''
        print(os.environ.get('ENV_IS_CI')," is ENV_IS_CI")
        print(os.environ.get['CI_DB_HOST']," is the host")
        time.sleep(5)
        assert 200 == 200

    def test_2(self):
        '''
            To test homepage
        '''
        time.sleep(5)
        assert 200 == 200
    
    def test_3(self):
        '''
            To test homepage
        '''
        time.sleep(5)
        assert 200 == 200
    
    def test_4(self):
        '''
            To test homepage
        '''
        time.sleep(5)
        assert 200 == 200
    
    def test_5(self):
        '''
            To test homepage
        '''
        time.sleep(5)
        assert 200 == 200
    
    def test_6(self):
        '''
            To test homepage
        '''
        time.sleep(5)
        assert 200 == 200
    
    def test_7(self):
        '''
            To test homepage
        '''
        time.sleep(5)
        assert 200 == 200
    
    def test_8(self):
        '''
            To test homepage
        '''
        time.sleep(5)
        assert 200 == 200
    
    def test_9(self):
        '''
            To test homepage
        '''
        time.sleep(5)
        assert 200 == 200
    
    def test_10(self):
        '''
            To test homepage
        '''
        time.sleep(5)
        assert 200 == 200
    