#!/usr/bin/env python

import sys
from utils import resource, multiple_replace
import subprocess
import os
import os.path

def LatexString(char):
    latexChar = open(resource('resources','char.tex')).read()
    latexChar = multiple_replace({'PYCHARGEN_STATS_OVERVIEW':_statsString(char),
                                  'PYCHARGEN_COMMON_SKILLS_OVERVIEW':_skillOverviewString(char),
                                  'PYCHARGEN_RESISTANCES_OVERVIEW':_resistanceString(char),
                                  'PYCHARGEN_SKILL_FULLLIST':_skillFullListString(char),
                                  'PYCHARGEN_CHARACTER_NAME':char.GetMisc('Name'),
                                  'PYCHARGEN_LEVEL':str(char.GetMisc('Level')),
                                  'PYCHARGEN_PROFESSION':char.GetMisc('Profession'),
                                  },latexChar)
    return latexChar

def SaveLatexFile(char,filename):
    with open(filename,'w') as f:
        f.write(LatexString(char))

def CompileLatex(char,filename):
    outputdir = os.path.dirname(filename)
    jobname = os.path.splitext(os.path.basename(filename))[0]
    latexChar = LatexString(char)
    if sys.platform=='win32':
        executable = resource('resources','pdftex.exe')
    else:
        executable = 'pdflatex'
        with open(os.devnull,'w') as shutup:
            if subprocess.call(['which',executable],stdout=shutup,stdin=shutup):
                raise EnvironmentError("""Could not find pdflatex.  Please install using 'sudo apt-get texlive-latex-base'""")
    args = [executable,
            '-output-directory='+resource('resources'),
            '-jobname='+jobname,
            "'"+latexChar+"'"]
    subprocess.call(args)
                     


def _statsString(char):
    return '\n'.join('\\Stat{{{name}}}{{{value}}}{{{bonus}}}'.format(
                            name=st.Name,value=st.Value,bonus=st.Bonus())
                     for st in char.Stats)

def _skillOverviewString(char):
    return '\n'.join('\\CommonSkill{{{name}}}{{{ranks}}}{{{bonus}}}'.format(
                            name=sk.Name,ranks=sk.Value,bonus=sk.Bonus())
                     for sk in char.Skills if sk.CommonlyUsed)

def _resistanceString(char):
    return '\n'.join('\\Resistance{{{name}}}{{{bonus}}}'.format(
                            name=res.Name,bonus=res.Bonus())
                     for res in char.Resistances)

def _skillFullListString(char):
    return '\n'.join('\\DetailSkill{{{name}}}{{{ranks}}}{{{bonus}}}{{{depth}}}'.format(
                           name=sk.Name,ranks=sk.Value,bonus=sk.Bonus(),depth=sk.Depth)
                     for sk in char.Skills)
