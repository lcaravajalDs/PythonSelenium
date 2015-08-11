from distutils.core import setup
setup(name='Python',
      packages=['Config','Elements', 'Locators', 'Page','Suites' ,'Tests'],
      package_dir= {'Config':'Config'},
      package_data={'Config': ['config.ini','Browsers/*.py','Env/*.py']}
      )
'''
Created on 5/8/2015

@author: Luciano
'''
