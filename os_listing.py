# -*- coding: utf-8 -*-
"""
Ed Matthews  
10-9-19

Tenable python connection test
"""

from tenable.sc import TenableSC
sc = TenableSC('insert your tenable url here')
sc.login('login', 'password')
for vuln in sc.analysis.vulns():
    ('listos', '=', 'Windows')
# Change above OS
    print(vuln)
