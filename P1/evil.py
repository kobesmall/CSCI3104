#!/usr/bin/python
# -*- coding: ISO-8859-1 -*- 
blob = """ 
    ���|�8J�_�N��f󪬈w�t	EV{�@G����hE��ٴ�,�k�u�t}c/"�q�H�R6m=[utEq2�4�;��7��`]��S��V<wgwL�UUO�����eq��g׳�"""
from hashlib import sha256
print(sha256(blob.encode()).hexdigest()) 
if(sha256(blob.encode()).hexdigest() == "648dda7e86ff7db5aa2c2e8bfc2f9d87518663c3a99e4a56b94c1a6db9debb65"):
	print("Prepare to be destroyed!")
elif(sha256(blob.encode()).hexdigest() == "ef096ff767522c1e74e3f0c2e92c51b0323f941ba875abae02731e34afc54f3a"):
	print("I come in peace.")